import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.common.validators import only_letters_validator, MinDateValidator

UserModel = get_user_model()


class Pet(models.Model):
    NAME_MAX_LENGTH = 30
    MIN_DATE = datetime.date(1920, 1, 1)
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=(
            MinDateValidator(MIN_DATE),
        )
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user', 'name')


class PetsPhoto(models.Model):
    photo = models.ImageField()

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
