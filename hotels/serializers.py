from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework import serializers
from .models import Rooms, Book, Spots
from users.serializers import UserSerializer


def check_existing_room(**kwargs):
    existing_room = Rooms.objects.filter(
        spot=kwargs['spot'],
        name=kwargs['name'],

    ).exists()
    if existing_room:
        return True


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

    def validate(self, attrs):

        if attrs['max_members'] < 0:
            raise ValidationError('인원은 1인 이상부터 가능 합니다!')

        if attrs['max_members'] < 0 or attrs['max_members'] > 10:
            raise ValidationError('인원은 1인 이상부터 가능 합니다! 최대 인원은 10명까지입니다.')

        if check_existing_room(name=attrs['name'], spot=attrs['spot']):
            raise ValidationError('이미 존재 하는 Room입니다!')
        return attrs


class DetailSerializer(serializers.ModelSerializer):
    book_set = serializers.SerializerMethodField()

    def get_book_set(self, obj):
        books = Book.objects.filter(room_id=obj.id)
        # print(books)
        book_list = BookSerializer(books, many=True)
        return book_list.data

    class Meta:
        model = Rooms
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('max_members'):
            if attrs['max_members'] < 0 or attrs['max_members'] > 10:
              raise ValidationError('인원은 1인 이상부터 가능 합니다! 최대 인원은 10명까지입니다.')
        return attrs

    def update(self, instance, validated_data):
        room = super().update(instance, validated_data)
        room.save()
        return room


class SpotSerializer(serializers.ModelSerializer):
    all_room = serializers.SerializerMethodField()

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


class BookSerializer(serializers.ModelSerializer):

    def get_user(self, obj):
        print(obj.user.email)
        return obj.user.email

    class Meta():
        extra_kwargs = {"user": {"required":False}, "room": {"required":False}}
        model = Book
        fields = '__all__'


class BookViewSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields ='__all__'


class BookInfoSerializer(serializers.ModelSerializer):
    user_set = serializers.SerializerMethodField()

    def get_user_set(self, obj):
        user = obj.user
        user_list = UserSerializer(user)
        return user_list.data

    class Meta():
        model = Book
        fields = '__all__'


class BookUserListSerializer(serializers.ModelSerializer):
    book_set = serializers.SerializerMethodField()

    def get_book_set(self, obj):
        books = Book.objects.filter(room_id=obj.id)
        book_list = BookInfoSerializer(books, many=True)
        return book_list.data

    class Meta:
        model = Rooms
        fields = ['name', 'book_set', 'status']

