from django.db import models
from .models import CarRequest, Cars
from rest_framework import serializers



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'title', 'image']


class CarRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRequest
        fields = ['car', 'name', 'email', 'phone', 'interest']

