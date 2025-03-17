from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ReserveModel


class ReserveAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request,*args,**kwargs):
        # "name": nameController.text,
        # "sname": snameController.text,
        # "phone": phoneController.text,
        # "date": dateController.text,
        # "count": countController.text,
        # "house": houseController.text,
        name = request.data.get('name')
        if name is None:
            return Response({"status":'failed','message':"Укажите своё имя!"})
        sname = request.data.get('sname')
        if sname is None:
            return Response({"status":'failed','message':"Укажите свою фамилию!"})
        phone = request.data.get('phone')
        if phone is None:
            return Response({"status":'failed','message':"Укажите свой номер телефона!"})
        date = request.data.get('date')
        if date is None:
            return Response({"status":'failed','message':"Укажите дату бронирования"})
        count = request.data.get('count')
        if count is None:
            return Response({"status":'failed','message':"Укажите количество отдыхающих"})
        house = request.data.get('house')
        if house is None:
            return Response({"status":'failed','message':"Укажите название дома!"})
        new_reserve = ReserveModel.objects.create(name=name,sname=sname,phone=phone,date=date,count=count,house=house)