from rest_framework.views import APIView
from .models import Review
from hotels.models import Rooms, Book
from .serializers import ReviewSerializer,ReviewCreateSerializer, RoomSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response   
from rest_framework import permissions



    #숙소 상세 조회, 리뷰 조회
class RoomDetail(APIView):
    def get(self, request, booked_id):
        room_review = get_object_or_404(Rooms, id=booked_id) #booked_id에 해당하는 숙소
        serializer = RoomSerializer(room_review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, booked_id):
        book = get_object_or_404(Book, id=booked_id) #booked_id에 해당하는 예약
        if book.user_id == request.user.id: #booked_id에 해당하는 예약자만 리뷰달 수 있게 
            serializer = ReviewCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(room = book.room, user=request.user, booked=book)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("권한이 없습니다.", status=status.HTTP_401_UNAUTHORIZED)


# 숙소 리뷰 CRUD
class ReviewDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, room_id):
        review = get_object_or_404(Review, id=room_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, room_id):
        review = get_object_or_404(Review, id=room_id)
        if request.user == review.user:
            serializer = ReviewCreateSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, room_id):
        review = get_object_or_404(Review, id=room_id)
        if request.user == review.user:
            review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)