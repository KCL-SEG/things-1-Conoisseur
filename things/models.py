from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Things(models.Model):
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
          validators=[MinValueValidator(0),MaxValueValidator(100)]
     )

