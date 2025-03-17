from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ServiceSerializer
from .models import ServiceModel



class ServiceAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        if pk:
            try:
                instance = ServiceModel.objects.get(pk=pk)
            except:
                return Response({'status':'failed','message':"Услуга не найдена!"})
            return Response({'status':'success','message':ServiceSerializer(instance).data})
        else:
            houses = ServiceModel.objects.all()
            return Response({'status': 'success', 'message': ServiceSerializer(houses,many=True).data})