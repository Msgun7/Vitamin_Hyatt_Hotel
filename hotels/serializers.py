from rest_framework import serializers
from hotels.models import Rooms, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta():
        model = Rooms
        fields = '__all__'