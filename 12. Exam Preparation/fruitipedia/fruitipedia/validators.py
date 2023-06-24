from django.core.exceptions import ValidationError


def first_char_is_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def fruit_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')