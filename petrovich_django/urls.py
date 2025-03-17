"""
URL configuration for petrovich_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import os

from django.contrib import admin
from django.urls import path
from album.views import AlbumAPIView
from houses.views import HouseAPIView
from enjoys.views import EnjoyAPIView
from services.views import ServiceAPIView
from django.views.static import serve
from reserves.views import ReserveAPIView
from django.conf.urls.static import static
from . import settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLUTTER_WEB_APP = os.path.join(BASE_DIR, 'landing')

def flutter_redirect(request, resource):
    return serve(request, resource, FLUTTER_WEB_APP)
urlpatterns = [
    path('', lambda r: flutter_redirect(r, 'index.html')),
    path('landing/', lambda r: flutter_redirect(r, 'index.html')),
    path('landing/<path:resource>', flutter_redirect),
    path('admin/', admin.site.urls),
    path('album/',AlbumAPIView.as_view()),
    path("reserve/",ReserveAPIView.as_view()),
    path('album/<int:pk>/',AlbumAPIView.as_view()),
    path('houses/',HouseAPIView.as_view()),
    path('houses/<int:pk>/',HouseAPIView.as_view()),
    path('enjoy/',EnjoyAPIView.as_view()),
    path('enjoy/<int:pk>/',EnjoyAPIView.as_view()),
    path('service/',AlbumAPIView.as_view()),
    path('service/<int:pk>/',ServiceAPIView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) if settings.DEBUG else []