from django.db import models
from authentication.models import User 

# Create your models here.

class User(models.Model):
    id = models.ForeignKey()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Favorites(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()