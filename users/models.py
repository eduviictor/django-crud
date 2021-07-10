 
from django.db import models


class User(models.Model):
    SEXO_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Not Specified")
    )

    username = models.TextField(max_length=30, unique=True)
    name = models.TextField(max_length=30)
    lastName = models.TextField(max_length=30, blank=True, null=True)
    profileImageUrl = models.TextField(blank=True, null=True)
    bio = models.TextField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=13, choices=SEXO_CHOICES, default="M")
    def __str__(self):
        return self.username
    