from django.db import models

# Create your models here.

class student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()
    

class Car(models.Model):
    car_name = models.CharField(max_length=200)
    speed = models.IntegerField(default=60)

    def __str__(self) -> str:
        return self.car_name
    

class Demo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)