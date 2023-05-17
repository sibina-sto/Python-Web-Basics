from django.core.exceptions import ValidationError


def plant_name_validator(value):
    for x in value:
        if not x.isalpha():
            raise ValidationError("Plant name should contain only letters!")
