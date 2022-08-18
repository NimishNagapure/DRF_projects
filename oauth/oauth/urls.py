"""oauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import urls
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url


router =  DefaultRouter()
router.register(r'singer',views.SingerViewSet,basename='singer')
router.register(r'song',views.SongViewSet,basename='song')
# router.register(r'^sign_up/$',views.SignUp,basename='sign_up')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^o/',include('oauth2_provider.urls', namespace ='oauth2_provider')),
    # url(r'^sign_up/$',include(views.SignUp.as_view(),namespace ='sign_up'))
    url(r'^signup/$', views.SignUp, name='signup'),

]