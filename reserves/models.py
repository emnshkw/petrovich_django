from django.db import models

class ReserveModel(models.Model):
    name = models.TextField("Имя клиента",default='')
    sname = models.TextField("Фамилия клиента",default='')
    phone = models.TextField("Номер телефона клиента",default='')
    date = models.TextField("Дата бронирования",default='')
    count = models.IntegerField("Количество человек",default='')
    house = models.TextField("Название дома",default='')


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'