# from multiprocessing import reduction
# from django.http import JsonResponse
# from django.shortcuts import render

# from watchlist_app.models import Movie

# # Create your views here.


# def movies_list(request):
#     movies = Movie.objects.all()

#     data = {
#         "movies":list(movies.values())
#     }

#     return JsonResponse(data)

# def movies_detail(request,id):
#     movies = Movie.objects.get(id=id)
#     print(movies)
#     data = {
#         "name" : movies.name,
#         "description":movies.description,
#         "active" : movies.active
#     }
#     return JsonResponse(data)