from django.db import models


class Breed(models.Model):
    """Breed model"""
    breed_type = models.CharField(
        max_length=100,
        null=True
    )
    hunting_type = models.CharField(
        max_length=100,
        null=True
    )
