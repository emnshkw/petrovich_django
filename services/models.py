from django.db import models
from photos.models import ImageModel


class ServiceModel(models.Model):
    title = models.TextField("Название услуги", default="")
    photo = models.ImageField("Изображение услуги", blank=True)
    price_on_card = models.TextField("Цена на карточке", default="")
    price = models.TextField("Цена в карточке", default="")
    description = models.TextField("Описание", default='')
    images = models.ManyToManyField(ImageModel,name='images',verbose_name='Изображения')


    def __str__(self):
        return f"Название услуги - {self.title}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
