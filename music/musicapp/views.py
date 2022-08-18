from .models import Album, Musician
from django.shortcuts import render
from .serializers import MusicianSerializer,AlbumSerializer
from .models import Musician,Album
from rest_framework import viewsets

# Create your views here.

class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer