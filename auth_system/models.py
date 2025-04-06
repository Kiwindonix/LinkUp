from django.contrib.auth.models import AbstractUser
from django.db import models

def get_default_dict():
    return {
        'theme': 'light',
    }


class CustomUser(AbstractUser):
    settings = models.JSONField(default=get_default_dict)
    image = models.ImageField(upload_to='profile/', default='default.jpg')
    profession = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.username}'
