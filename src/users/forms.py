from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UsernameField
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation, get_user_model


class RegisterForm(UserCreationForm):
    password1_attrs = {
        'name': 'password',
        'autocomplete': 'new-password',
        'placeholder': 'new password'
    }

    password2_attrs = {
        'autocomplete': 'new-password',
        'placeholder': 'confirm password'
    }

    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs=password1_attrs),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(attrs=password2_attrs),
        strip=False,
        help_text=_('Enter the same password as before, for verification.'),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'new username'}),
        }


class LoginForm(AuthenticationForm):
    username_attrs = {
        'autofocus': True,
        'placeholder': 'username',
    }

    password_attrs = {
        'autocomplete': 'current-password',
        'placeholder': 'password',
    }

    username = UsernameField(widget=forms.TextInput(attrs=username_attrs))
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs=password_attrs),
    )
