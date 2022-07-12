from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from iBeat.models import Post

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    names = models.CharField(blank=True, max_length=120)
    bio=models.CharField(max_length=60)
    email = models.EmailField(max_length=100, blank=True)
   
   

    
    def __str__(self):
        return f'{self.user.username} Profile'
    
   

