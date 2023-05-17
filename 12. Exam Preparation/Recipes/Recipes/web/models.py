from django.core.validators import MinValueValidator
from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LEN = 30
    INGREDIENTS_MAX_LEN = 250

    TIME_MIN_VALUE = 0

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    description = models.TextField()

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LEN,
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)',
        validators=(
            MinValueValidator(TIME_MIN_VALUE),
        )
    )
