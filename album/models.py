from django.db import models
from photos.models import ImageModel


class AlbumModel(models.Model):
    title = models.TextField("Название",default='')
    images = models.ManyToManyField(ImageModel,name='images',null=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'