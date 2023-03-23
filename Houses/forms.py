from django import forms
from .models import House_Details

class House_DetailsForm(forms.ModelForm):
    class Meta:
        model =House_Details
        fields = ('location', 'title', 'description', 'monthly_rent', 'thumbnail',)