"""
users models
"""

from django.db import models


class ExampleUserModel(models.Model):
    example_field = models.CharField(max_length=255)

