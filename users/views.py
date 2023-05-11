from rest_framework.views import APIView
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from hotels.serializers import BookSerializer
from users.models import User
from hotels.models import Rooms
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from users.serializers import UserSerializer,LoginSerializer,UserProfileSerializer,UserUpdateSerializer

class SignupView(APIView):
     def post(self, request):
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'message':' 가입완료!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(TokenObtainPairView):
    serializer_class=LoginSerializer
    
class UserProfileView(APIView):
    def get(self, request, user_id):
        user_profile = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, user_id):
        user_profile = get_object_or_404(User, id=user_id)
        serializer = UserUpdateSerializer(user_profile,data=request.data,partial=True)
        if request.user == user_profile:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('권한이 없습니다!', status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            user.delete()
            return Response('삭제되었습니다!', status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)   

# 마이페이지 내 리뷰 조회, 내 예약 조회
class MyPage(APIView):
    def get(self, request, user_id):
        review = Review.objects.filter(user=user_id)
        book = Review.objects.filter(user=user_id)
        serializer = ReviewSerializer(review, many=True)
        bookserializer = BookSerializer(book, many=True)
        data = {
            'reviews': serializer.data,
            'books': bookserializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)