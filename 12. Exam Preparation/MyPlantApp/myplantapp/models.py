from django.db import models
from django.core.validators import MinLengthValidator

from myplantapp.validators import plant_name_validator


TYPE = (
    ("Outdoor Plants", "Outdoor Plants"),
    ("Indoor Plants", "Indoor Plants"),
)


class PlantModel(models.Model):
    type = models.CharField(
        verbose_name="Type",
        max_length=14,
        choices=TYPE
    )

    name = models.CharField(
        verbose_name="Name",
        validators=[
            MinLengthValidator(2),
            plant_name_validator
        ],
        max_length=20
    )

    image_url = models.URLField(
        verbose_name="Image URL"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    price = models.FloatField(
        verbose_name="Price"
    )
