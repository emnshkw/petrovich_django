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
        files = os.listdir('/home/petrovich_django/media/')
        names = []
        a = ord('а')
        alp = ''.join([chr(i) for i in range(a,a+32)]) + ' '
        for file in files:
            file = file.split('.')[0]
            word = ''
            for i in range(len(file)):
                if file[i] in alp:
                    word += file[i]
            names.append(word)
        print(names)
        if pk:
            try:
                instance = AlbumModel.objects.get(pk=pk)
            except:
                return Response({'status':'failed','message':"Альбом не найден!"})
            return Response({'status':'success','message':AlbumSerializer(instance).data})
        else:
            albums = AlbumModel.objects.all()
            return Response({'status': 'success', 'message': AlbumSerializer(albums,many=True).data})