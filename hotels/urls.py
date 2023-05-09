from django.contrib import admin
from django.urls import path, include
from hotels import views

urlpatterns = [
    path('room/',views.RoomView.as_view(), name='room'),
    path('book/',views.RoomView.as_view(), name='book'),
]
