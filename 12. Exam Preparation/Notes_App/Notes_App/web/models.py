from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    AGE_MIN_VALUE = 0

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        verbose_name='Last Name',
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )

    image_url = models.URLField(
        verbose_name='Link to Profile Image',
    )


class Note(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image_url = models.URLField(
        verbose_name='Link to Image',
    )

    content = models.TextField()
