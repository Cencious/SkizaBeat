from re import M
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')


class Album(models.Model):
    album_title = models.CharField(max_length=120)
    artist = models.CharField(max_length=100)
    album_image = models.FileField(upload_to='album_logo/')

    def __str__(self):
        return self.album_title

class Artist(models.Model):
    name = models.CharField(max_length=60)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

class Song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    artist =models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.FileField(upload_to='song/')
    image = CloudinaryField('image')
    song_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.song
    