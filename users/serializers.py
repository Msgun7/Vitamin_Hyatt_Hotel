from rest_framework import serializers
from .models import User, Review
from hotels.models import Rooms, Book


class RoomSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True,read_only=True)
  
    class Meta:
        model = Rooms
        fields = ['id', 'reviews', 'room_name', 'max_members', 'description', 'price']
        

class ReviewSerializer(serializers.ModelSerializer):
    # room = RoomSerializer(read_only = True)
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'booked', 'room', 'title', 'context', 'stars']
        extra_kwargs = {
            'user': {'read_only': True},
            'booked': {'read_only': True},
        }


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'context', 'stars')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','user')
