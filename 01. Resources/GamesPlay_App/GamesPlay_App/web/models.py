from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15

    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD = 'Board/Card Game'
    OTHER = 'Other'
    CATEGORIES = [(x, x) for x in (ACTION, ADVENTURE, PUZZLE, STRATEGY, SPORTS, BOARD, OTHER)]

    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0

    MAX_LEVEL_MIN_VALUE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CATEGORIES,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        )
    )

    image_url = models.URLField()

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MAX_LEVEL_MIN_VALUE),
        )
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
