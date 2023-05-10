from django.urls import path
from . import views

urlpatterns = [
    path('room/<int:booked_id>/', views.RoomDetail.as_view()),
    path('<int:room_id>/', views.ReviewDetail.as_view())
]
