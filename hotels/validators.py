from rest_framework.serializers import ValidationError
from .models import Rooms

def check_existing_room(**kwargs):
    # if len(attrs['max_members']) < 0:
    #     raise ValidationError("인원이 0보다 작을 수 없습니다!")
    existing_room = Rooms.objects.filter(
        spot=kwargs['spot'],
        name=kwargs['name']
    ).exists()
    if existing_room:
        return True