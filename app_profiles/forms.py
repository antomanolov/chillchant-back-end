from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from app_profiles.appuser import AppUser

class CustomCreationFrom(UserCreationForm):
    
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Confirm the password'} ),
        
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Confirm the password'}),
        strip=False,
        
    )
    class Meta:
        model = AppUser
        fields = ("email",)
        widgets ={
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
            })
        }
        

class CustomAuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Enter your email'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'placeholder': 'Enter your password'}),
    )
    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": ("This account is inactive."),
    }

    