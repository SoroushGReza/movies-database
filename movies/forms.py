from django import forms
from django.forms import ModelForm
from .models import Review, UserProfile


# Login Form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# User Profile Form
class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=False, label="E-mail")
    new_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="New Password"
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Confirm New Password"
    )

    class Meta:
        model = UserProfile
        fields = ['email', 'new_password', 'confirm_new_password']


# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
        rating = forms.ChoiceField(
            choices=RATING_CHOICES, widget=forms.RadioSelect
        )
