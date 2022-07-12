from email.policy import default
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.forms import ImageField
from iBeat.models import Post 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    image = CloudinaryField('image', default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    name = models.CharField(blank=True, max_length=120)
    bio = models.CharField(max_length=60 ,blank=True)
    email = models.EmailField(max_length=100, blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='posts', blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
        
