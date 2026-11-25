from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "display_name",
            "password1",
            "password2"
        )
        labels = {
            "display_name": "Display name"
        }
        help_texts = {
            "display_name": "Optional name shown on your public profile."
        }
        error_messages = {
            "username": {
                "unique": "This username is already taken.",
                "required": "Enter a username."
            },
            "email": {
                "invalid": "Enter a valid email address."
            }
        }

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Choose a username"}
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "you@example.com"}
        )
    )
    display_name = forms.CharField(
        required=False,
        max_length=80,
        widget=forms.TextInput(
            attrs={"placeholder": "How should other users see you?"}
        )
    )

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "autofocus": True
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password"}
        )
    )

    error_messages = {
        "invalid_login": "The username or password is incorrect.",
        "inactive": "This account is inactive."
    }


class ProfileForm(forms.ModelForm):
    username = forms.CharField(
        disabled=True,
        help_text="Your username cannot be changed."
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "display_name",
            "bio",
            "avatar"
        )
        labels = {
            "display_name": "Display name",
            "bio": "About you"
        }
        help_texts = {
            "bio": "Maximum 500 characters."
        }
        error_messages = {
            "email": {
                "invalid": "Enter a valid email address."
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["display_name"].widget.attrs["placeholder"] = (
            "Your public display name"
        )
        self.fields["bio"].widget.attrs["placeholder"] = (
            "Tell other members about yourself"
        )

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        duplicates = User.objects.filter(
            email__iexact=email
        ).exclude(pk=self.instance.pk)

        if duplicates.exists():
            raise forms.ValidationError(
                "Another account already uses this email address."
            )
        return email