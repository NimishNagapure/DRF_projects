from django.shortcuts import render
from .serializers import SingerSerializer,SongSerializer,SignUpSerializer
from rest_framework import viewsets
from .models import Singer,Song,User
from django.db import connection
from rest_framework import generics
from .permissions import IsAuthenticatedOrCreated


# Create your views here.

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreated)

class SingerViewSet(viewsets.ModelViewSet):
    queryset= Singer.objects.all()
    serializer_class=SingerSerializer
    

class SongViewSet(viewsets.ModelViewSet):
    queryset= Song.objects.all()
    serializer_class=SongSerializer   
