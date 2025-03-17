from django.db import models


class ImageModel(models.Model):
    description = models.TextField("Описание",blank=True)
    image = models.ImageField('Фотография', null=True)

    def __str__(self):
        return f'ID - {self.id}. {self.description}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'