"""SkizaBeat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views

from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('profile',user_views.UserProfileViewSet)
router.register('login',user_views.LoginViewSet,basename='login')
router.register('feed',user_views.UserProfileFeedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload',user_views.UploadView.as_view(),name='file-upload'),
    path('',include(router.urls)),
    
    path('', include('rest_framework.urls'))
    
]
