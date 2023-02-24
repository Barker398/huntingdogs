from django.db import models


class Trait(models.Model):
    """Trait model"""
    description = models.CharField(
        max_length=200,
        null=True
    )
