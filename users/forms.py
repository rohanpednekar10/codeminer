from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(help_text="")
    password1 = forms.CharField(label= "Password",
                                widget=forms.PasswordInput,
                                help_text= "")
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput,
                                help_text= "")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class BioUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
