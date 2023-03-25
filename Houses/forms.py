from django import forms
from .models import House_Details, MultipleImage

class House_DetailsForm(forms.ModelForm):
    class Meta:
        model =House_Details
        fields = ('location', 'title', 'description', 'monthly_rent', 'thumbnail', 'owners_contact', 'available',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'description'})

class MultipleImagesForm(forms.ModelForm):
    class Meta:
        model = MultipleImage
        fields = ['images']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs.update({'multiple': True})
        
