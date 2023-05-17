import re

from django.core.exceptions import ValidationError

REGEX_VALIDATION_MESSAGE = 'This field must contain only ingredient separated with ",".'
REGEX_USERNAME = "^[A-Za-z,]*$"


def regex_validator(value):
    regex = REGEX_USERNAME
    if not re.match(regex, value):
        raise ValidationError(REGEX_VALIDATION_MESSAGE)
