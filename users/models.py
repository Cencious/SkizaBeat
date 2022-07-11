from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)


class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''This is a userprofile class'''

    email=models.EmailField(max_length=50,unique=True)
    name=models.CharField(max_length=100)
    profile_picture = CloudinaryField('pictures/',default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

       

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Get users full name'''

        return self.name
    
    def get_short_name(self):
        '''Get short name'''

        return self.name

    def __str__(self):
        
        return self.email

class ProfileFeedItem(models.Model):

    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text=models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.status_text

