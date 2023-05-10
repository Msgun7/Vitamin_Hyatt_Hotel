from django.urls import path
from users import views

urlpatterns = [
    path('signup/',views.UserView.as_view(), name='signup'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),  
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('<int:room_id>', views.RoomDetailReviewList.as_view()),
    path('reviews/<int:review_id>', views.ReviewDetail.as_view()),
    path('profile/<int:user_id>', views.MyPage.as_view())
]

