from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model

# Create your models here.
class Things(Model):
     name = models.CharField(
          unique=True,
          blank=False,
          max_length=30
     )
     description = models.CharField(
          unique=False,
          blank=False,
          max_length=120
     )
     quantity = models.IntegerField(
          unique=False,
          max_length=100,

     )