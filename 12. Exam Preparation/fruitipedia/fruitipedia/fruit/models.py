from django.db import models
from django.core import validators
from ..validators import fruit_name_only_letters


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2),
            fruit_name_only_letters
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )
