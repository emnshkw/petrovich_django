from django.db import models
from photos.models import ImageModel


class EnjoyModel(models.Model):
    title = models.TextField("Название развлечения", default="")
    photo = models.ImageField("Изображение развлечения", blank=True)
    price_on_card = models.TextField("Цена на карточке", default="")
    price = models.TextField("Цена в карточке", default="")
    description = models.TextField("Описание", default='')
    images = models.ManyToManyField(ImageModel,name='images',verbose_name='Изображения')

    def __str__(self):
        return f"Название развлечения - {self.title}"


    class Meta:
        verbose_name = "Развлечение"
        verbose_name_plural = "Развлечения"

