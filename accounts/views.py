from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from Houses.forms import House_DetailsForm, MultipleImagesForm
from Houses.models import House_Details, MultipleImage
from django.contrib import messages
from .forms import SignUpForm
from django.core.paginator import Paginator

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
def owner_detail(request, pk):
    user = User.objects.get(pk=pk)
    houses = user.houses.exclude(available=False)
    paginator = Paginator(houses, 5)
    page_number = request.GET.get('page', 1)
    my_listing = paginator.get_page(page_number)

    return render(request, 'userprofile/owner_detail.html',
                  {'user': user,
                   'my_listing': my_listing})

@login_required
def user_admin(request):
    houses = request.user.houses.exclude(available=False)
    paginator = Paginator(houses, 5)
    page_number = request.GET.get('page', 1)
    my_listing = paginator.get_page(page_number)

    return render(request, 'userprofile/user_admin.html',
                  {'my_listing': my_listing})

@login_required
def add_house(request):
    house_form = House_DetailsForm()
    images_form = MultipleImagesForm()
    if request.method == "POST":
        files = request.FILES.getlist('images')
        house_form = House_DetailsForm(request.POST, request.FILES)

        if house_form.is_valid():
            title = request.POST.get('title')
            slug = slugify(title)

            house = house_form.save(commit=False)
            house.user = request.user
            house.slug = slug
            house.save()

            for file in files:
                MultipleImage.objects.create(house=house, images=file)

            messages.success(request, 'The house was added successfuly!')

            #return redirect('payments:process')

            return redirect('user_admin')
    else:
        house_form = House_DetailsForm()
        images_form = MultipleImagesForm()



    context = {"h_form": house_form, "i_form": images_form, "title": "Add House"}
    return render(request, 'Agency/add_house.html', context )

@login_required
def edit_house(request, pk):
    house = House_Details.objects.filter(user=request.user).get(pk=pk)
    
    if request.method == 'POST':
        form = House_DetailsForm(request.POST, request.FILES, instance=house)
        


        if form.is_valid():
            form.save()

            messages.success(request, 'The changes were submitted successfully!')

            return redirect('user_admin')

    else:
        form = House_DetailsForm(instance=house)
        

    context = {"form": form, "house": house, "title": "Edit House"}

    return render(request, 'Agency/edit_house.html', context)
    

@login_required
def delete_house(request, pk):
    house = House_Details.objects.filter(user=request.user).get(pk=pk)
    house.available = False
    house.save()

    messages.success(request, 'The house was deleted successfully!')

    return redirect('user_admin')
