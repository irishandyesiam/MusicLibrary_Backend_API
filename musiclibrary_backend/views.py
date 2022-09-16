from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song
from musiclibrary_backend import serializers

@api_view(['GET', 'POST'])

def musiclibrary_list(request):

    if request.method == 'GET':
        musiclibrary_songs = Song.objects.all()
        serializer = SongSerializer(musiclibrary_songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def musiclibrary_detail(request, pk):
    if request.method == 'GET':
        try:
            song = Song.objects.get(pk=pk)
            serializer = SongSerializer(song)
            return Response(serializer.data)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method =='PUT':
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
   