from rest_framework.views import APIView
from .models import Review, User
from hotels.models import Rooms
from .serializers import ReviewSerializer,ReviewCreateSerializer,BookSerializer,RoomSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response



    #숙소 상세 조회, 리뷰 조회
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
    def post(self, request,  review_id):
      room = get_object_or_404(Rooms, id=review_id)
      serializer = ReviewCreateSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(room = room, user = User.objects.all().order_by("?")[0]) #모든 유저 랜덤 정렬 하고 1번째 유저 가져오기
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
