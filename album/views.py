import os

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import AlbumModel
from photos.models import ImageModel


class AlbumAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        print(os.listdir("/home/petrovich_django/media/"))
        if pk:
            try:
                instance = AlbumModel.objects.get(pk=pk)
            except:
                return Response({'status':'failed','message':"Альбом не найден!"})
            return Response({'status':'success','message':AlbumSerializer(instance).data})
        else:
            albums = AlbumModel.objects.all()
            return Response({'status': 'success', 'message': AlbumSerializer(albums,many=True).data})