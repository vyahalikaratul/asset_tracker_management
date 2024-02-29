from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    """
    Custom authentication form for logging in users.

    This form extends the default AuthenticationForm provided by Django to include an email field.
    Users can log in using either their username or email address.
    """
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label='Remember Me', required=False)