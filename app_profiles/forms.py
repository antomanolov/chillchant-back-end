from django.contrib.auth.forms import UserCreationForm

from app_profiles.appuser import AppUser

class CustomCreationFrom(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ("email",)
        