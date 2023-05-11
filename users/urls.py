from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),  
    path('<int:room_id>', views.RoomDetailReviewList.as_view()),
    path('reviews/<int:review_id>', views.ReviewDetail.as_view()),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='profile'),
]
    
    #     path('profile/<int:user_id>', views.MyPage.as_view())
