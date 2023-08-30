from django.forms import ValidationError


def only_alpha(string):
    if not string.isalpha():
        raise ValidationError('Please enter only letters')