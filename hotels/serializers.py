from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Rooms, Book, Spots


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

    def update(self, instance, validated_data):
        room = super().update(instance, validated_data)
        room.save()
        return room


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spots
        fields = '__all__'
