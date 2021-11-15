from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class CharactersValidator(UnicodeUsernameValidator):
    regex = r'^[a-zA-Z0-9]*$'
    message = _(
        'Enter a valid username. This value may contain only letters and '
        'numbers.'
    )
