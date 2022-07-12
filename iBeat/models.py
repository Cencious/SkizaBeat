from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .helper import get_audio_length, validate_is_audio


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')

    def __str__(self):
        return f'{self.name} Post'


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
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    artist =models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.FileField(upload_to='songs/')
    image = CloudinaryField('image')
    song_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.song_title)
    
    
    
# class Music(models.Model):
#     title=models.CharField(max_length=500)
#     artiste=models.CharField(max_length=500)
#     album=models.ForeignKey('Album',on_delete=models.SET_NULL,null=True,blank=True)
#     time_length=models.DecimalField(max_digits=20, decimal_places=2,blank=True)
#     audio_file=models.FileField(upload_to='musics/',validators=[validate_is_audio])
#     cover_image=models.ImageField(upload_to='music_images/')

#     def save(self,*args, **kwargs):
#         if not self.time_length:
#             # logic for getting length of audio
#             audio_length=get_audio_length(self.audio_file)
#             self.time_length =f'{audio_length:.2f}'

#         return super().save(*args, **kwargs)

#     class META:
#         ordering="id"


# class Album(models.Model):
#     name=models.CharField(max_length=400, null=True)










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
