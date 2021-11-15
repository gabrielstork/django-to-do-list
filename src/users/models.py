from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from . import validators


class User(AbstractUser):
    min_length_validator = MinLengthValidator(
        limit_value=3,
        message=_('At least 3 characters are required.')
    )

    characters_validator = validators.CharactersValidator()

    username = models.CharField(
        _('username'),
        max_length=15,
        primary_key=True,
        help_text=_('Required. 3-15 characters. Letters and numbers only.'),
        validators=[characters_validator, min_length_validator],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )

    first_name = None
    last_name = None

    REQUIRED_FIELDS = []
