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