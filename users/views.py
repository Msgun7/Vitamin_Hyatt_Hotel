from rest_framework.views import APIView
from reviews.models import Review
from reviews.serializers import ReviewSerializer, myBookSerializer, ReviewCreateSerializer
from users.models import User,AdminUser
from hotels.models import Book, Rooms
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from users.serializers import UserSerializer, LoginSerializer, UserProfileSerializer, UserUpdateSerializer,AdminUserSerializer



class SignupView(APIView):
     def post(self, request):
        data = request.data.copy()
        data['phone'] = request.data['phone'].replace('-', '').strip()
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': ' 가입완료!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    serializer_class=LoginSerializer
  
class MyPage(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, user_id):
        try:
            admin = get_object_or_404(AdminUser, admin_user=request.user)
            serializer = AdminUserSerializer(admin)
            if admin:
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            user_profile = get_object_or_404(User, id=user_id)
            review = Review.objects.filter(user=user_id)
            book = Book.objects.filter(user=user_id)
            serializer = ReviewSerializer(review, many=True)
            bookserializer = myBookSerializer(book, many=True)
            profileserializer = UserProfileSerializer(user_profile)
            data = {
                'reviews': serializer.data,
                'books': bookserializer.data,
                'profile': profileserializer.data,
            }
            return Response(data, status=status.HTTP_200_OK)

    def patch(self, request, user_id):
        user_profile = get_object_or_404(User, id=user_id)
        data = request.data.copy()
        
        if 'phone' in request.data:
            data['phone'] = request.data['phone'].replace('-', '').strip()
        
        serializer = UserUpdateSerializer(
            user_profile, data=data, partial=True)


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

class MyReviewCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, booked_id):
        book = get_object_or_404(Book, id=booked_id)  # booked_id에 해당하는 예약
        print(book)
        if book.user_id == request.user.id:  # user_id에 해당하는 예약자만 리뷰달 수 있게
            serializer = ReviewCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(room=book.room, user=request.user, booked=book)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("권한이 없습니다.", status=status.HTTP_401_UNAUTHORIZED)

class ReviewDetail(APIView):
    # 리뷰 상세 조회
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, review_id):
        review = get_object_or_404(Review, user=request.user, id=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, review_id):
        review = get_object_or_404(Review, user=request.user, id=review_id)
        serializer = ReviewCreateSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        permission_classes = [permissions.IsAuthenticated]
        review = get_object_or_404(Review, user=request.user, id=review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
