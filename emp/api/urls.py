from django.contrib import admin
from api import views
from django.urls import path
from .views import *


urlpatterns = [
    path('leftjoin/', LeftJoin.as_view()), 
    path('innerjoin/', InnerJoin.as_view()),
    path('fullouterjoin/', FullOuterJoin.as_view()), 
    path('rightjoin/', RightJoin.as_view()),

]
