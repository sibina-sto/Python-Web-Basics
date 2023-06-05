from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator


def name_validator(value: str):
    if not value[0].upper():
        raise ValidationError("Your name must start with a capital letter!")


def only_letters_validator(value: str):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Plant name should contain only letters!")


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    PROFILE_NAMES_MAX_LEN = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        verbose_name='Username',
        validators=[MinLengthValidator(USERNAME_MIN_LEN)],
        null=False,
        blank=False,
        # unique=True,
    )

    first_name = models.CharField(
        max_length=PROFILE_NAMES_MAX_LEN,
        verbose_name='First Name',
        validators=[name_validator],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=PROFILE_NAMES_MAX_LEN,
        verbose_name='Last Name',
        validators=[name_validator],
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Profile'


PLANT_TYPES = (
    ("Outdoor Plants", "Outdoor Plants"),
    ("Indoor Plants", "Indoor Plants"),
)


class Plant(models.Model):
    TYPE_MAX_LEN = 14
    PLANT_NAME_MAX_LEN = 20
    PLANT_NAME_MIN_LEN = 2

    plant_type = models.CharField(
        max_length=TYPE_MAX_LEN,
        verbose_name='Plant Type',
        choices=PLANT_TYPES,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=PLANT_NAME_MAX_LEN,
        verbose_name='Name',
        validators=[MinLengthValidator(PLANT_NAME_MIN_LEN), only_letters_validator],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name='Description',
        null=False,
        blank=False,
    )

    price = models.FloatField(
        verbose_name='Price',
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Plant'
