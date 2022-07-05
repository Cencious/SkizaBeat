from django.urls import path
from . import views

urlpatterns= [
    path('login/',views.login_api),
    path('user/', views.get_user_data),
    path('register/', views.register_api),
]