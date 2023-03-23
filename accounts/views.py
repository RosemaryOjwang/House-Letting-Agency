from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from Houses.forms import House_DetailsForm
from Houses.models import House_Details, House_Location

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
    return render(request, 'Agency/add_house.html')