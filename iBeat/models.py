from re import T
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .helper import get_audio_length, validate_is_audio


# Create your models here.

class Album(models.Model):
    album_title = models.CharField(max_length=120, null=True)
    artist = models.CharField(max_length=100, null=True)
    album_image = models.FileField(upload_to='album_logo/', null=True)

    def __str__(self):
        return str(self.album_title)

class Artist(models.Model):
    name = models.CharField(max_length=60, null=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

class Song(models.Model):

    title= models.CharField(max_length=60, null=True)
    album=models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    Singer_name =models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    image= CloudinaryField('image')
    song = models.FileField(blank=True,null=True,upload_to='songs/')
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20, null=True, blank=True)
    genre = models.CharField(max_length=50, null=True, blank=True)
    paginate_by = 2
 
    def __str__(self):
        return str(self.title)
    
    
    
