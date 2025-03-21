# Generated by Django 5.1.3 on 2024-11-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', verbose_name='Название дома')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Изображение дома')),
                ('price', models.TextField(default='', verbose_name='Цена за день')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
        ),
    ]
