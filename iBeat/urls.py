from django.urls import path
from iBeat import views 
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.index, name='index'),
    path('search/', views.search_playlist, name='search'),
    # path('albums/', views.albums_list, name='albums'),
    # path('albums/<int:id>', views.albums_details, name='albumsd'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

# this will help to serve uploaded images on the development server
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)