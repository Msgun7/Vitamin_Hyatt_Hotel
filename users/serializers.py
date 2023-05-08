from rest_framework import serializers
from .models import User, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'booked', 'room', 'title', 'context', 'stars']
        # extra_kwargs = {
        #     'user': {'read_only': True},
        #     'booked': {'read_only': True},
        #     'room': {'read_only': True},
        # }