from rest_framework import serializers
from .models import HouseModel
from photos.serializers import ImageSerializer


class HouseSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True,many=True)
    class Meta:
        model = HouseModel
        fields = '__all__'