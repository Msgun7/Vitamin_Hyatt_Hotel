from django.urls import path
from hotels import views

urlpatterns = [
    path('', views.RoomViewAPI.as_view()),
    path(''),
]