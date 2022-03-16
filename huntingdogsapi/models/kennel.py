from django.db import models

class Kennel(models.Model):
    """kennel model"""
    name = models.CharField(
        max_length=50,
        null=True
    )
    image_url = models.CharField(
        max_length=500,
        null=True
    )
    