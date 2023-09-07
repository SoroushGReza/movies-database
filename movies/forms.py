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
        required=False,
        label="New Password"
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        label="Confirm New Password"
    )

    class Meta:
        model = UserProfile
        fields = ['email', 'new_password', 'confirm_new_password']

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password or confirm_new_password:
            if new_password != confirm_new_password:
                self.add_error(
                    'confirm_new_password',
                    "New password and confirm new password do not match"
                )

        return cleaned_data


# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
        rating = forms.ChoiceField(
            choices=RATING_CHOICES, widget=forms.RadioSelect
        )
