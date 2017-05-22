from django import forms
from django.contrib.auth.models import User
from .models import SignUser
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password", )