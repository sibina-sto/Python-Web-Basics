from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def only_letters_validator(value):
    if not all(ch.isalpha for ch in value):
        raise ValidationError('Value must contain only letters!')


@deconstructible
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Value must be greater than {self.min_date}')
