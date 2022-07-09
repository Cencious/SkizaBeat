from django.shortcuts import render

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

# def search_playlist(request):
#     if request.method == 'GET':
#         name = request.GET.get("title")
#         results = Playlist.objects.filter(albums__icontains=Albums).all()
#         print(search_playlist)
#         message = f'name'
#         params = {
#             'results': results,
#             'message': message
#         }
#         return render(request, 'search.html', params)
#     else:
#         message = "You haven't searched for any playlist category"
#     return render(request, "iBeat/search.html")