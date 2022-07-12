from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):

    email= forms.EmailField()
    class Meta:
        model = User
        fields =['username','email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()

    class Meta:
        model = User
        fields =['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image','bio']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)