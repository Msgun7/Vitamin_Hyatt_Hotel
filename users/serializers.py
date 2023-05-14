from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User,AdminUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("비밀번호와 비밀번호 확인이 일치하지않습니다!")
        return data

    def create(self, validated_data):
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
        password = validated_data.get('password') # password 값 가져오기
        if password is not None: # password 값이 존재하는 경우에만 실행
            user = super().update(instance, validated_data)
            user.set_password(password)
            user.save()
        else:
            user = super().update(instance, validated_data)
            user.save()
        return user


class LoginSerializer(TokenObtainPairSerializer): 
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        token['is_admin'] = user.is_admin
        
        return token


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'point',)


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'
