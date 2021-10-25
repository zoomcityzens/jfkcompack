from django.db import models
from django.utils import timezone
from uuid import uuid4




class Cars(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to="car_images", default="car.jpg")
    description = models.CharField(max_length=50, default="Duis vitae consequat neque. Nulla pharetra eleifend nulla")
    timestamp = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return f"{self.title}"
    

class CarRequest(models.Model):
    ACTION = [
        ('swap', 'swap'),
        ('upgrade', 'upgrade')
    ]

    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    interest = models.CharField(choices=ACTION, max_length=7)
    timestamp = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return f"{self.name} | interest: {self.interest} | {self.timestamp}"
    
