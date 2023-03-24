from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from Houses.forms import House_DetailsForm
from Houses.models import House_Details, House_Location
from django.contrib import messages
# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
def owner_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/owner_detail.html',
                  {'user': user})

@login_required
def user_admin(request):
    return render(request, 'userprofile/user_admin.html' )

@login_required
def add_house(request):
    if request.method == "POST":
        form = House_DetailsForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            slug = slugify(title)

            house = form.save(commit=False)
            house.user = request.user
            house.slug = slug
            house.save()

            messages.success(request, 'The house was added successfuly!')

            return redirect('user_admin')
    else:
        form = House_DetailsForm()

    return render(request, 'Agency/add_house.html',
                  {'title': 'Add House',
                  'form': form})

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

    return render(request, 'Agency/edit_house.html',
                  {'title': 'Edit House',
                  'form': form})
