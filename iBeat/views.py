from django.shortcuts import redirect, render
from .models import Artist,Album,Song
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'iBeat/index.html')

def home(request):
    songs = Song.objects.all()
    artists = Artist.objects.all()
    return render(request, 'iBeat/home.html', {'songs':songs, 'artists':artists})


def discover(request):
    albums = Album.objects.all()
    musics = Song.objects.filter(album__album_title__icontains=albums)
    return render(request, 'iBeat/discover.html', {'musics':musics, 'albums':albums})

def dashboard(request):
    songs = Song.objects.all()
    return render(request, 'iBeat/dashboard.html' ,{'songs':songs})

def playlist(request):
   songs = Song.objects.all()
   artists = Artist.objects.all()
   return render(request, 'iBeat/playlist.html', {'songs':songs, 'artists':artists})

def search_playlist(request):
    if 'songs' in request.GET and request.GET["song"]:
        search_term = request.GET.get("song")
        searched_songs = Song.search_by_title(search_term).all()
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"projects": searched_songs})
    else:
        message = "You haven't searched for any projects yet"
    return render(request, 'search.html', {'message': message})

# def search_playlist(request):
#     songs = Song.objects.all()
#     queryset = request.GET.get('search')
#     if queryset is not None:
#         songs = songs.filter(song__icontains = queryset)

#         if songs:
#             return render(request, {'songs':songs}, 'home.html')
#         elif songs:
#             songs = songs.filter(artist__name__icontains=queryset)
#             return render(request, 'home.html',{'songs':songs})
#         elif songs:
#             songs = songs.filter(album__album_title__icontains=queryset)
#             return render(request, 'home.html',{'songs':songs})
#         else:
#             messages.error(request, 'Enter a valid name')
#             return redirect('home')
#     return render(request, "iBeat/search.html")
    

# @login_required(login_url='/accounts/login/')
# def search_results(request):
#   if 'playlist' in request.GET and request.GET["playlist"]:
#     search_term = request.GET.get('playlist')
#     searched_users = Playlist.search_playlist(search_term)
#     message = f"{search_term}"
#     return render(request,'iBeat/search.html',{"message":message,"results":searched_users})
#   else:
#     message="You haven't searched for any term."  
#     return render(request,'iBeat/search.html',{"message":message,"results":searched_users})

def Albums(request):
    albums = Album.objects
    return render(request, 'Albums.html', {'Albums': albums})


def Albums_songs(request, name):
    musics = Song.objects.filter(album__album_title=name)
    return render(request, 'Albums_songs.html', {'Musics': musics})


def Song_player(request):
    songs = Song.objects
    artists = Artist.objects
    return render(request, 'home.html', {'songs': songs})


def Artists(request):
    artists = Artist.objects
    return render(request, 'Artist.html', {'Artists': artists})


def Artist_songs(request, name):
    artist = Song.objects.filter(artist__name=name)
    return render(request, 'Artist_songs.html', {'Artist': artist})

