from django.db import models
from authentication.models import User 

# Create your models here.

class Favorites(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()