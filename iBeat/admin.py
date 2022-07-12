from django.contrib import admin
from .models import  Song, Album,Artist

# Register your models here.
# admin.site.register(Post)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)

