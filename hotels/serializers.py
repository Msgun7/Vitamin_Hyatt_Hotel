from rest_framework import serializers
from .models import Rooms



class RoomsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

# 만들었다. 시리얼라이저 했다. 내가
# plus plus