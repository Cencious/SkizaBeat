from django.contrib import admin
from .models import Album, Artist, Post, Song

# Register your models here.
admin.site.register(Post)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)

