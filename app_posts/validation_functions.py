from django.core.exceptions import ValidationError


def image_size_validation(file_obj):
    if file_obj.file.size > 5 * 1024 * 1024:
        raise ValidationError('Image size must be max 5MB')