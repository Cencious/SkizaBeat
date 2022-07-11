# from django.http import HttpResponseRedirect
# from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.decorators import login_required
from .models import Playlist, Artists, Songs, Albums
# from django.contrib.auth.models import User


# from .serializers import AlbumsSerializer
# from .models import Albums
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# # from django.shortcuts import get_object_or_404
# # from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# # import filters


# Create your views here

def search_playlist(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Playlist.objects.filter(albums__icontains=Albums).all()
        print(search_playlist)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any playlist category"
    return render(request, "search.html")


# class AlbumsList(APIView):

# @api_view(['GET','POST'])  
# def albums_list(request):
#         if request.method =='GET':

#           Albums1 = Albums.objects.all()
#           serializer = AlbumsSerializer(Albums1, many=True)
#         # filter_backends = (filters.SearchFilter,)
#         # search_fields = ('artists','songs', 'album')

#           return JsonResponse({'Albums':serializer.data})

#         if request.method =='POST':
#           serializer = AlbumsSerializer(data=request.data) 
#           if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)    

# @api_view(['GET','PUT','DELETE'])
# def albums_details(request, id):
#        try:
#           Albums1 = Albums.objects.get(pk=id)
#        except Albums.DoesNotExist:
#          return Response(status=status.HTTP_404_NOT_FOUND) 
  
#        if request.method =='GET':
#          serializer = AlbumsSerializer(Albums1)
#          return Response(serializer.data)

#        elif request.method =='POST':
#          serializer = AlbumsSerializer(Albums1, data=request.data)
#          if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

#        elif request.method =='DELETE':
#          Albums1.delete() 
#          return Response(status=status.HTTP_204_NO_CONTENT)

# def post(self):
    #    pass  

































































































  