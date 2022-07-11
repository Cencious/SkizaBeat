from re import M
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')

    def __str__(self):
        return f'{self.name} Post'


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
    
    
    

# class Playlist(models.Model):
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='playlist')
#     title = models.CharField(blank=False,max_length=100)
#     image = CloudinaryField('image')
#     post_date =models.DateField(auto_now=True)
    
#     def __str__(self):
#         return f'{self.title} Playlist'
    
#     def create_playlist(self):
#         self.save()

#     def delete_playlist(self):
#         self.delete()

#     @classmethod
#     def search_playlist(cls, name):
#         return cls.objects.filter(name__icontains=name).all()
