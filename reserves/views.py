from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ReserveModel
import requests
import vk_api
from vk_api.longpoll import VkLongPoll


def send_message(phone):
    vk = vk_api.VkApi(token='vk1.a.y73Kz_6U78IOt2prsBEzDSp-7GKjAwJi4Skd3oVqBtMD1aMZwMLyr0r8lkVGtUSTG0HCemy5Fh1Xfv-5oyCkPyWwcK3qgofckYlxbqynAFQ1B2-gkDongG4osQcHfNywXk9UGsrqEyTf_b7uA5ItvqwEo_9-QA7MYfWEPJw2HczvhxHHuX-zNzcm6oWGl7IB')
    longpoll = VkLongPoll(vk)
    post = {
        'user_id': 235396096,
        'message': f"Новое бронирование от {phone}",
        'random_id': 0
    }

    vk.method('messages.send', post)

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
        send_message(phone)
        return Response({"status": 'success', 'message': "Бронирование добавлено!"})