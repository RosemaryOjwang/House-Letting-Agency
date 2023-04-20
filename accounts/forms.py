from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'emailField'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        #self.fields['username'].widget.attrs['class':'usernameField']
        #self.fields['password1'].widget.attrs['class':'password1Field']
        #self.fields['password2'].widget.attrs['class':'password2Field']
