from rest_framework import serializers
from .models import Rooms



class RoomsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

