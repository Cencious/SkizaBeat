
from django.shortcuts import redirect, render

from iBeat.forms import UploadMusic
from .models import Song, Album, Artist
# from django.core.paginator import Paginator
# from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'iBeat/index.html')

def home(request):
     
    # paginator= Paginator(Song.objects.all(),1)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # context={"page_obj":page_obj}
    songs = Song.objects.all()
    return render(request, 'iBeat/home.html', {'songs':songs})

def discover(request):
    albums = Album.objects.all()
    # musics = Song.objects.filter(album__album_title__icontains=albums)
    return render(request, 'iBeat/discover.html', { 'albums':albums})

def dashboard(request):
    songs = Song.objects.all()
    return render(request, 'iBeat/dashboard.html', {'songs':songs} )

def playlist(request):
   songs = Song.objects.all()
   artists = Artist.objects.all()
   albums = Album.objects.all()
   return render(request, 'iBeat/playlist.html', {'songs':songs, 'artists':artists, 'albums':albums})


def Upload(request):
    form = UploadMusic()
    if request.POST:
        form = UploadMusic(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            Singer_name = form.cleaned_data.get('Singer_name')
            if Singer_name:
                artist_name = Artist.objects.get_or_create(name=Singer_name)
                instance.Singer_name = artist_name[0]
                instance.save()
                return redirect('home')
            else:
                instance.save()
                return redirect('home')
        return redirect('home')   
    return render(request, 'iBeat/upload.html', {'form':form})