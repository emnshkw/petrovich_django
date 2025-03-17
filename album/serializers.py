from rest_framework import serializers
from .models import AlbumModel
from photos.serializers import ImageSerializer

class AlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True,many=True)
    class Meta:
        model = AlbumModel
        fields = '__all__'