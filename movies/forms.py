from django import forms
from .models import Movie
from django.forms import ModelForm
from .models import Movie


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
