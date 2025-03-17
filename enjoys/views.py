from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EnjoySerializer
from .models import EnjoyModel



class EnjoyAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        if pk:
            try:
                instance = EnjoyModel.objects.get(pk=pk)
            except:
                return Response({'status':'failed','message':"Развлечение не найдено!"})
            return Response({'status':'success','message':EnjoySerializer(instance).data})
        else:
            houses = EnjoyModel.objects.all()
            return Response({'status': 'success', 'message': EnjoySerializer(houses,many=True).data})