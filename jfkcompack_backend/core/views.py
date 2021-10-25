import json

from django.shortcuts import render
from django.http import JsonResponse
from .serializer import CarRequestSerializer, CarSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import CarRequest, Cars




def index(request, *args, **kwargs):
    return  render(request, 'core/index.html')


class CarViewSet(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    permission_class = [AllowAny]

class CarRequestViewSet(ModelViewSet):
    queryset = CarRequest.objects.all()
    serializer_class = CarRequestSerializer
    permission_class = [AllowAny]


