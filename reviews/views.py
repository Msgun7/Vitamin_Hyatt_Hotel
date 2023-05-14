from rest_framework.views import APIView
from .models import Review
from hotels.models import Rooms
from .serializers import RoomSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

# 숙소 상세 조회, 리뷰 조회
class RoomDetail(APIView):
    def get(self, request, room_id):
        room_review = get_object_or_404(
            Rooms, id=room_id)  # room_id에 해당하는 숙소
        serializer = RoomSerializer(room_review)
        return Response(serializer.data, status=status.HTTP_200_OK)

