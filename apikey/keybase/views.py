from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly




# Create your views here.

class Nimish_API(APIView):
    permission_classes = [HasAPIKey | IsAuthenticated ]

    def get(self, request,pk=None,format=None):
        id=pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    

    
# assign-work
# 7wJow0v3.9533UpKyHkptBZD9HmojlFSEDDSyE3hJ




# JgL7sa88.uq2PHB6TR9J120kkcbOyj2Ik96d8EQbi




# curl -H 'Api-Token: YOUR_API_TOKEN_HERE' -H 'Api-Secret-Key: YOUR_API_SECRET_KEY_HERE' http://localhost:8000/stdapi/
# curl -H 'my-app:1sZt2PXt.TwBLQvYais1bV4K4mXvDITOlFrXx0o0C' http://localhost:8000/stdapi/
# curl -H 'Api-Token:1sZt2PXt' -H 'Api-Secret-Key:TwBLQvYais1bV4K4mXvDITOlFrXx0o0C' http://localhost:8000/stdapi/






                # key = request.META["HTTP_AUTHORIZATION"].split()[1]
        # api_key = APIKey.objects.get_from_key(key)
        # project = Student.objects.get(api_key=api_key)