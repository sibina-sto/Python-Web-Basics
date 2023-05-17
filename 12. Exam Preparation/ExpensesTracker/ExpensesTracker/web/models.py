from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from ExpensesTracker.validators import only_letters_validator, MaxFileSizeInMbValidator


class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 15

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 15

    DEFAULT_BUDGET = 0
    MIN_VALUE_BUDGET = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_FIRST_NAME),
            only_letters_validator,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_LAST_NAME),
            only_letters_validator,
        ),
    )

    budget = models.FloatField(
        default=DEFAULT_BUDGET,
        validators=(
            MinValueValidator(MIN_VALUE_BUDGET),
        ),
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    MAX_LEN_TITLE = 30

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
    )

    image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('title', 'price')
