from django.db import models
from .breed import Breed
from .kennel import Kennel
from .trait import Trait


class Dog(models.Model):
    """Dog model"""
    name = models.CharField(max_length=30)
    image_url = models.CharField(max_length=500, null=True)
    breed = models.ForeignKey(
        Breed,
        related_name="dog",
        on_delete=models.CASCADE
    )
    kennel = models.ForeignKey(
        Kennel,
        related_name="dogs",
        on_delete=models.CASCADE
    )
    traits = models.ManyToManyField(Trait)
