from iBeat import views as iBeat_views
from django.urls import path

urlpatterns =[
    
    path('home/',iBeat_views.home, name='home'),
    path('',iBeat_views.index, name='index'),
    path('discover/',iBeat_views.discover, name='discover'),
    path('dashboard/',iBeat_views.dashboard, name='dashboard'),
    path('playlist/',iBeat_views.playlist, name='playlist'),
    path('search/', iBeat_views.search_playlist, name='search'),
]
