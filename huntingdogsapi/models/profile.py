from django.contrib.auth.models import User
from django.db import models

from huntingdogsapi.models.dog import Dog


class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    bio = models.CharField(
        max_length=150,
        default="Bio not created yet"
    )
    address = models.CharField(
        max_length=200,
        null=True
    )
    phoneNumber = models.CharField(max_length=200, null=True)
    email = models.CharField(
        max_length=100,
        null=True
    )
    favorites = models.ManyToManyField(Dog)
