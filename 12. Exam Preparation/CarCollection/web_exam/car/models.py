from django.db import models
from django.core import validators

from .validators import valid_car_year


class Car(models.Model):
    CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other')
    )

    type = models.CharField(
        max_length=10,
        choices=CHOICES,
        null=False,
        blank=False,
    )
    model = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(2, 'Model should have at least 2 characters')],
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[valid_car_year]
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(1)]
    )
