from django.core.validators import MinLengthValidator
from django.db import models
from authapp.validators import profile_name_validator


class ProfileModel(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2),
        ]
    )

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=20,
        validators=[
            profile_name_validator
        ]
    )

    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=20,
        validators=[
            profile_name_validator
        ]
    )

    profile_picture = models.URLField(
        verbose_name="Profile Picture",
        null=True,
        blank=True
    )
