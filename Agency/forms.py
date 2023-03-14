from django import forms
from django.forms import ModelForm
from .models import Image, House_Details, House_Location

class House_LocationForm(ModelForm):
    class Meta:
        model = House_Location
        fields = "__all__"
class HouseForm(ModelForm):
    category_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Size of the house"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Features of the house"}))
    rent_amount = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Rent per month"}))
    available = forms.BooleanField(widget=forms.BooleanField(attrs={"class": "form-control", "placeholder": "Is it available"}))
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))
    class Meta:
        model = House_Details
        fields = "__all__"
         

class ImageForm(ModelForm):
    images = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "multiple":True}))
    class Meta:
        model = Image
        fields = ['images']