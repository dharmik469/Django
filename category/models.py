from django.db import models

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)                                                            

class Email(models.Model):
    email = models.EmailField()
    contact = models.IntegerField()
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)