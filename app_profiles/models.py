from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from app_profiles.validators import only_alpha


class AppUser(AbstractUser):
    MIN_CHARS = 2
    USERNAME_MAX_CHARS = 15
    FIRST_LAST_NAME_MAX_CHARS = 40

    email = models.EmailField(
        unique=True,
    )
    username = models.CharField(
        max_length=USERNAME_MAX_CHARS,
        validators=(
            MinLengthValidator(MIN_CHARS),
        ),
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=FIRST_LAST_NAME_MAX_CHARS,
        validators=(
            MinLengthValidator(MIN_CHARS),
            only_alpha,
        ),
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=FIRST_LAST_NAME_MAX_CHARS,
        validators=(
            MinLengthValidator(MIN_CHARS),
            only_alpha,
        ),
        null=True,
        blank=True,
    )

    bio = models.TextField(
        null=True,
        blank=True
    )

    profile_picture = models.ImageField()

    last_profile_edit = models.DateTimeField(
        auto_now=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
