from django.contrib import admin

from users.models import UserProfile,ProfileFeedItem,User

# Register your models here.

admin.site.register(User)

admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)

