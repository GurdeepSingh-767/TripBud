from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        

class TripPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPhotos
        fields = '__all__'