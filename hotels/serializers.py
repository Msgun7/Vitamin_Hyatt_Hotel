from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Rooms, Book, Spots
from .validators import check_existing_room


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

    def validate(self, attrs):
        if attrs['max_members'] < 0:
            raise ValidationError('인원은 1인 이상부터 가능 합니다!')
        if check_existing_room(name=attrs['name'], spot=attrs['spot']):
            raise ValidationError('이미 존재 하는 Room입니다!')
        return attrs


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('max_members'):
            if attrs['max_members'] < 0:
                raise ValidationError('인원은 1인 이상부터 가능 합니다!')
        return attrs

    def update(self, instance, validated_data):
        room = super().update(instance, validated_data)
        room.save()
        return room


class SpotSerializer(serializers.ModelSerializer):
    all_room = serializers.SerializerMethodField()
    # total_room2 = DetailSerializer(many=True, read_only=True)

    def get_all_room(self, obj):
        all_rooms = Rooms.objects.filter(spot=obj)
        rooms = RoomsSerializer(all_rooms, many=True)
        return rooms.data

    class Meta:
        model = Spots
        fields = '__all__'

    def update(self, instance, validated_data):
        spot = super().update(instance, validated_data)
        spot.save()
        return spot

