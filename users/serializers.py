from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hotels.models import Rooms, Book
from users.models import User,AdminUser,Review
from django.core.exceptions import ValidationError
from .validators import check_phone, check_password,check_username

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
    password2 = serializers.CharField(write_only=True, required=True)
     
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("비밀번호와 비밀번호 확인이 일치하지않습니다!")
        return data
        
    def create(self,validated_data):
        validated_data.pop('password2')
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('password','phone',)       
    
    def update(self,instance, validated_data):
        if validated_data.get('password'):
            check_password(validated_data['password'])
        
        if validated_data.get('phone'):
            check_phone(validated_data['phone'])
            
        user = super().update(instance,validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
        
class LoginSerializer(TokenObtainPairSerializer): 
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        return token
    
class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','email', 'phone','point',)
    
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
