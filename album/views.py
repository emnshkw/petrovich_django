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
            if '_' in file:
                os.remove(f'/home/petrovich_django/media/{file}')
                continue
            file = file.split('.')[0]
            word = ''
            for i in range(len(file)):
                if file[i].lower() in alp:
                    word += file[i]
            names.append(word)
        names = list(set(names))
        name_and_files = {}
        for name in names:
            if name not in name_and_files.keys():
                name_and_files[name] = []
            for file in files:
                if name in file:
                    name_and_files[name].append(file)
        # for name in name_and_files.keys():
        #     album = AlbumModel.objects.create(title=name)
        #     for file in name_and_files[name]:
        #         image = ImageModel.objects.create(description=file,image=file)
        #         album.images.add(image)
        #     album.save()
        if pk:
            try:
                instance = AlbumModel.objects.get(pk=pk)
            except:
                return Response({'status':'failed','message':"Альбом не найден!"})
            return Response({'status':'success','message':AlbumSerializer(instance).data})
        else:
            albums = AlbumModel.objects.all()
            return Response({'status': 'success', 'message': AlbumSerializer(albums,many=True).data})