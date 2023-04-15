from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from Houses.forms import House_DetailsForm, MultipleImagesForm
from Houses.models import House_Details, MultipleImage
from django.contrib import messages
# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
def owner_detail(request, pk):
    user = User.objects.get(pk=pk)
    houses = user.houses.exclude(available=False)

    return render(request, 'userprofile/owner_detail.html',
                  {'user': user,
                   'houses': houses})

@login_required
def user_admin(request):
    houses = request.user.houses.exclude(available=False)
    return render(request, 'userprofile/user_admin.html',
                  {'houses': houses} )

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

            return redirect(reverse('payments:process'))

            #return redirect('user_admin')
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
        

    context = {"form": form, "title": "Edit House"}

    return render(request, 'Agency/edit_house.html', context)
    

@login_required
def delete_house(request, pk):
    house = House_Details.objects.filter(user=request.user).get(pk=pk)
    house.available = False
    house.save()

    messages.success(request, 'The house was deleted successfully!')

    return redirect('user_admin')
