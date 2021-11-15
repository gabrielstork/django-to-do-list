from django import forms
from . import models


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'title', 'autofocus': True}
            ),
            'description': forms.TextInput(
                attrs={'placeholder': 'description'}
            ),
        }
