from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from .validators import check_password
from hotels.validators import validate_phone_number


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
            validate_phone_number(validated_data['phone'])
            
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
    
