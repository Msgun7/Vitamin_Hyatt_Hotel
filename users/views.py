from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from users.models import User

class UserView(APIView):
    pass

class CustomTokenObtainPairView(TokenObtainPairView):
    pass
    
class UserProfileView(APIView):
    pass