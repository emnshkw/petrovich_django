import os

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import AlbumModel
from photos.models import ImageModel
from houses.models import HouseModel
from enjoys.models import EnjoyModel
from services.models import ServiceModel


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
        for name in name_and_files.keys():
            name_and_files[name] = list(set(name_and_files[name]))
            for file in name_and_files[name]:
                ImageModel.objects.create(description=file, image=file)
        for name in name_and_files.keys():
            album = AlbumModel.objects.create(title=name)
            for file in name_and_files[name]:
                image = list(ImageModel.objects.filter(description=file))[0]
                album.images.add(image)
            album.save()
        # for name in name_and_files.keys():
        #     house = HouseModel.objects.create(title=name)
        #     count = 0
        #     for file in name_and_files[name]:
        #         count += 1
        #         image = ImageModel.objects.get(description=file)
        #         house.images.add(image)
        #         if count == 5:
        #             break
        #     house.save()
        # images = ImageModel.objects.all()
        # for image in images:
        #     with_name_imgs = list(ImageModel.objects.filter(description=str(image.description)))
        #     while len(with_name_imgs) > 1:
        #         poped = with_name_imgs.pop(0)
        #         poped.delete()
        for name in name_and_files.keys():
            house = HouseModel.objects.create(title=name)
            count = 0
            for file in name_and_files[name]:
                count += 1
                image = list(ImageModel.objects.filter(description=file))[0]
                house.images.add(image)
                if count == 5:
                    break
            house.save()
        for name in name_and_files.keys():
            enjoy = EnjoyModel.objects.create(title=name)
            count = 0
            for file in name_and_files[name]:
                count += 1
                image = list(ImageModel.objects.filter(description=file))[0]
                enjoy.images.add(image)
                if count == 5:
                    break
            enjoy.save()
        for name in name_and_files.keys():
            service = ServiceModel.objects.create(title=name)
            count = 0
            for file in name_and_files[name]:
                count += 1
                image = list(ImageModel.objects.filter(description=file))[0]
                service.images.add(image)
                if count == 5:
                    break
            service.save()
        if pk:
            try:
                instance = AlbumModel.objects.get(pk=pk)
            except:
                return Response({'status':'failed','message':"Альбом не найден!"})
            return Response({'status':'success','message':AlbumSerializer(instance).data})
        else:
            albums = AlbumModel.objects.all()
            return Response({'status': 'success', 'message': AlbumSerializer(albums,many=True).data})