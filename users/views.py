from django.shortcuts import redirect
from rest_framework.views import APIView
from .models import Review, User, BasicUser
from hotels.models import Rooms
from .serializers import ReviewSerializer, ReviewCreateSerializer, BookSerializer, RoomSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from users.serializers import UserSerializer, LoginSerializer, BasicUserProfileSerializer


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': ' 가입완료!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


# 일반 회원 관리자 나누는 로직 -> 로그인 할 때 판단
class Test(APIView):
    def post(self, request):
        if request.user.is_staff == True:
            pass
        else:
            pass
        return redirect('/users/login')


class BasicUserProfileView(APIView):
    def get(self, request, user_id):
        basic_user_profile = get_object_or_404(BasicUser, basic_user_id=user_id)
        serializer = BasicUserProfileSerializer(basic_user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        basic_user_profile = get_object_or_404(User, basic_user_id=user_id)
        serializer = UserSerializer(basic_user_profile, data=request.data)
        if request.user == basic_user_profile:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('권한이 없습니다!', status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, user_id):
        user = get_object_or_404(User, basic_user_id=user_id)
        if request.user == user:
            user.delete()
            return Response('삭제되었습니다!', status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

            # 숙소 상세 조회, 리뷰 조회


class RoomDetailReviewList(APIView):
    def get(self, request, room_id):
        room_review = get_object_or_404(Rooms, id=room_id)
        serializer = RoomSerializer(room_review)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 숙소 리뷰 CRUD
class ReviewDetail(APIView):
    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, review_id):
        room = get_object_or_404(Rooms, id=review_id)
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(room=room, user=User.objects.all().order_by("?")[0])  # 모든 유저 랜덤 정렬 하고 1번째 유저 가져오기
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        # if request.user == review.user:
        serializer = ReviewCreateSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        # review = get_object_or_404(Review, id=review_id, user=request.user.review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
