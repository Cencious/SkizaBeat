from django.shortcuts import render

from iBeat.models import Playlist

# Create your views here.
def index(request):
    return render(request, 'iBeat/index.html')

def home(request):
    return render(request, 'iBeat/home.html')


def discover(request):
    return render(request, 'iBeat/discover.html')

def dashboard(request):
    return render(request, 'iBeat/dashboard.html')

def profile(request):
    return render(request, 'iBeat/profile.html')

def playlist(request):
    return render(request, 'iBeat/playlist.html')

# @login_required(login_url='/accounts/login/')
def search_results(request):
  if 'playlist' in request.GET and request.GET["playlist"]:
    search_term = request.GET.get('playlist')
    searched_users = Playlist.search_playlist(search_term)
    message = f"{search_term}"
    return render(request,'iBeat/search.html',{"message":message,"results":searched_users})
  else:
    message="You haven't searched for any term."  
    return render(request,'iBeat/search.html',{"message":message,"results":searched_users})