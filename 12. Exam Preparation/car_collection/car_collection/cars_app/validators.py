from django.core.exceptions import ValidationError


def valid_year_validator(value):
    if not 1980 <= value <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")
