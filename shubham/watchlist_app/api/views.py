
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def movies_list(reqest):
    if reqest.method == 'GET':
        movies =  Movie.objects.all()
        serializer = MovieSerializer(movies,many = True)
        return Response(serializer.data)
    if reqest.method == 'POST':
        serializer = MovieSerializer(data=reqest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def movies_detail(request,id):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=id)
        
        except Movie.DoesNotExist:
            return Response({'error':'Not found'},status=404)    
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'PUT':
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return Response(status=204)
