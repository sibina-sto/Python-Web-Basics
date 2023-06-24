from django.db import models
from django.core import validators
from ..validators import first_char_is_letter


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2),
            first_char_is_letter
        ]
    )

    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(1),
            first_char_is_letter
        ]
    )

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(8)
        ]
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=18,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
