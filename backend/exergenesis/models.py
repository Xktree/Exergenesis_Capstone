from django.db import models
from authentication.models import User 

# Create your models here.

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.IntegerField()
    longitude = models.IntegerField()