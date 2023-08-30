# Generated by Django 4.2.4 on 2023-08-30 05:18

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profiles', '0002_remove_appuser_user_name_alter_appuser_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
