from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)