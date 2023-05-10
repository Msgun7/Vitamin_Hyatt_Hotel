from django.urls import path
from . import views


urlpatterns = [
    path('<int:room_id>', views.RoomDetailReviewList.as_view()),
    path('reviews/<int:review_id>', views.ReviewDetail.as_view()),
    path('profile/<int:user_id>', views.MyPage.as_view())
]
