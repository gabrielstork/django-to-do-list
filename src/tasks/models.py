from django.db import models
from django.conf import settings


class Task(models.Model):
    task_id = models.CharField(max_length=8, primary_key=True, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.title}'
