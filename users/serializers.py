from rest_framework import serializers
from users.models import User, BasicUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
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


