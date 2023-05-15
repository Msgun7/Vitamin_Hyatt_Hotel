from rest_framework import serializers
from .models import Review
from hotels.models import Rooms, Book


class AllReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    review_set = AllReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Rooms
        fields = ['id', 'review_set', 'name',
                  'max_members', 'description', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    user = serializers.SerializerMethodField()
    booked = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()
    spot = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    def get_booked(self, obj):
        return obj.booked.created_at

    def get_room(self, obj):
        return obj.room.name

    def get_spot(self, obj):
        return obj.room.spot.name

    class Meta:
        model = Review
        fields = ['id', 'user', 'booked', 'room',
                  'title', 'context', 'stars', 'spot']
        extra_kwargs = {
            'user': {'read_only': True},
            'booked': {'read_only': True},
        }


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email


    class Meta:
        model = Review
        fields = ['id', 'user', 'booked', 'room',
                  'title', 'context', 'stars']
        extra_kwargs = {
            'user': {'read_only': True},
            'booked': {'read_only': True},
            'room': {'read_only': True},
        }

    def validate_booked(self, value):
        if value is None:
            raise serializers.ValidationError("Invalid booked value")
        return value


class myBookSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()
    spot = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    def get_room(self, obj):
        return obj.room.name

    def get_spot(self, obj):
        return obj.room.spot.name

    class Meta():
        model = Book
        fields = ['id', 'user', 'room', 'members',
                  'check_in', 'check_out', 'spot']
