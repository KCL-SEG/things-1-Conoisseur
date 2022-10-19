from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model

# Create your models here.
class Things(Model):
     name = models.CharField()
     description = models.CharField()
     quantity = models.IntegerField()