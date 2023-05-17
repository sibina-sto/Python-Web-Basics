from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection.cars_app.validators import valid_year_validator


class Car(models.Model):
    TYPES = (
        ("Sport Car", "Sport Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    )

    type = models.CharField(
        max_length=9,
        choices=TYPES
    )

    model = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=20
    )

    year = models.IntegerField(
        validators=[
            valid_year_validator,
        ]
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            MinValueValidator(1),
        ]
    )
