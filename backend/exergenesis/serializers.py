from rest_framework import serializers
from .models import User, Favorites

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password']
        depth = 1

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Favorites
        fields = ['id', 'latitude', 'longitude']
        depth = 1