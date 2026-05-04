from django.core.exceptions import ValidationError

def positive_integer(value):
    if value <= 0:
        raise ValidationError("Value must be a positive integer.")