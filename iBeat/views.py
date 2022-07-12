from django.shortcuts import redirect, render
from .models import Song,Album
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'iBeat/index.html')

def home(request):
    songs = Song.objects.all()
    # artists = Artist.objects.all()
    # musics=list(Music.objects.all().values())
    return render(request, 'iBeat/home.html', { 'songs':songs})

def discover(request):
    albums = Album.objects.all()
    # musics = Song.objects.filter(album__album_title__icontains=albums)
    return render(request, 'iBeat/discover.html', { 'albums':albums})

def dashboard(request):
    # songs = Song.objects.all()
    return render(request, 'iBeat/dashboard.html' )

def playlist(request):
    # all_songs = Song.objects.all()
    return render(request, 'iBeat/playlist.html')

def search_playlist(request):
    # songs = Song.objects.all()
    queryset = request.GET.get('search')
    if queryset is not None:
        songs = songs.filter(song__icontains = queryset)

        if songs:
            return render(request, {'songs':songs}, 'home.html')
        elif songs:
            songs = songs.filter(artist__name__icontains=queryset)
            return render(request, 'home.html',{'songs':songs})
        elif songs:
            songs = songs.filter(album__album_title__icontains=queryset)
            return render(request, 'home.html',{'songs':songs})
        else:
            messages.error(request, 'Enter a valid name')
            return redirect('home')
    return render(request, "iBeat/search.html")
    

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
