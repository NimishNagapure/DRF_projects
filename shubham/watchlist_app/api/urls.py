from unicodedata import name
from django.contrib import admin
from django.urls import path

from watchlist_app.api.views import movies_detail, movies_list

urlpatterns = [
    path("list/",movies_list ,name="movie-list"),
    path('<int:id>',movies_detail,name="movie-detail")
]
