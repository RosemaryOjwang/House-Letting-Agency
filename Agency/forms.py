from django import forms
from django.forms import ModelForm
from .models import Image, House_Details

class HouseForm(ModelForm):
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))
    class Meta:
        model = House_Details
        fields = ['thumbnail']
         

class ImageForm(ModelForm):
    images = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "multiple":True}))
    class Meta:
        model = Image
        fields = ['images']