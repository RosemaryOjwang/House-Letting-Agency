from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserRegister

#Create form

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserRegister
        fields = "__all__"

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user