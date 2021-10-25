from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CarRequestViewSet,
    CarViewSet
)


router = DefaultRouter()
router.register('cars', CarViewSet)
router.register('cars_request', CarRequestViewSet)


urlpatterns = []

urlpatterns += router.urls
