from rest_framework import serializers
from users.models import User, BasicUser, Review
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hotels.models import Rooms, Book


class UserSerializer(serializers.ModelSerializer):
    # password1 = serializers.CharField(write_only=True, required=True)
    # password2 = serializers.CharField(write_only=True, required=True)
    
    # class Meta:
    #     model = User
    #     fields = '__all__'
        
    # def validate(self, data):
    #     if data['password1'] != data['password2']:
    #         raise serializers.ValidationError("The two password fields didn't match.")
    #     return data
        
    # def create(self,validated_data):
    #     validated_data.pop('password2')
    #     user = User.objects.create_user(**validated_data)
    #     password = user.password
    #     user.set_password(validated_data['password1'])
    #     user.save()
    #     return user
    
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self,validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self,instance, validated_data):
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
    
class BasicUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicUser
        fields = '__all__'
        # fields = ('id','email','username', 'phone','point',)


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
