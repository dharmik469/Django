from django.db import models

# Create your models here.

class Car(models.Model):
    Car_name = models.CharField(max_length=200)
    About_car = models.TextField()
    Car_image = models.ImageField(upload_to='Car')