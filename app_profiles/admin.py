from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from app_profiles.appuser import AppUser


class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser


class CustomAdmin(UserAdmin):
    form = CustomChangeForm
    fieldsets = (
        ('User Info', {'fields': ('username', 'first_name', 'last_name', 'bio', 'profile_picture')}),
        ('Important dates', {'fields': ('last_login', 'date_joined',  'last_profile_edit')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),  # Move permission fields to this section
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('date_joined', 'last_login', 'email',  'last_profile_edit')
        return ()


admin.site.register(AppUser, CustomAdmin)


