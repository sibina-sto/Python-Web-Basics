from django.core.exceptions import ValidationError
from django.db import models


def validate_age(value):
    if value < 12:
        raise ValidationError('The age cannot be below 12')


def validate_float_rating(value):
    if not 0.1 <= value <= 5.0:
        raise ValidationError('The rating must be between 0.1 and 5.0 (both inclusive).')


def validate_max_level(value):
    if value < 1:
        raise ValidationError('The max level cannot be below 1')


class ProfileModel(models.Model):
    MAX_PASSWORD_LENGTH = 30
    NAMES_MAX_LENGTH = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(validate_age,),
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_PASSWORD_LENGTH,
    )
    first_name = models.CharField(
        blank=True,
        default='',
        max_length=NAMES_MAX_LENGTH,
    )
    last_name = models.CharField(
        blank=True,
        default='',
        max_length=NAMES_MAX_LENGTH,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class GameModel(models.Model):
    TITLE_MAX_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    CATEGORY_CHOICES = (
        ('ACTION', 'Action'),
        ('ADVENTURE', 'Adventure'),
        ('PUZZLE', 'Puzzle'),
        ('STRATEGY', 'Strategy'),
        ('SPORTS', 'Sports'),
        ('BOARD/CARD GAME', 'Board/Card game'),
        ('OTHER', 'Other'),
    )
    title = models.CharField(
        null=False,
        blank=False,
        max_length=TITLE_MAX_LENGTH,
        unique=True,
    )
    category = models.CharField(
        null=False,
        blank=False,
        max_length=CATEGORY_MAX_LENGTH,
        choices=CATEGORY_CHOICES,
    )
    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(validate_float_rating,)
    )
    max_level = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=(validate_max_level,),
        verbose_name='Max Level',
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
