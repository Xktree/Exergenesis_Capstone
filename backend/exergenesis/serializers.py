from rest_framework import serializers
from .models import Favorites

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Favorites
        fields = ['id', 'latitude', 'longitude']
        depth = 1