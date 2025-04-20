from django.db import models

# home/models.py
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
