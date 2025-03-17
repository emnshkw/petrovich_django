from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HouseSerializer
from .models import HouseModel



class HouseAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        if pk:
            try:
                instance = HouseModel.objects.get(pk=pk)
            except:
                return Response({'status':'failed','message':"Дом не найден!"})
            return Response({'status':'success','message':HouseSerializer(instance).data})
        else:
            houses = HouseModel.objects.all()
            return Response({'status': 'success', 'message': HouseSerializer(houses,many=True).data})