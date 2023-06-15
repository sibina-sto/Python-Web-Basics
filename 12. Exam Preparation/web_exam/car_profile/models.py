from django.db import models
from django.core import validators


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        validators=[validators.MinLengthValidator(2, 'The username must be a minimum of 2 chars')]
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(18)],
    )
    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def get_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return ''
