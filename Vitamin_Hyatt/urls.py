from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('manager/', include("hotels.urls")),
    path('users/', include('users.urls')),
=======
    path('users/', include('users.urls')),
    path('hotels/', include('hotels.urls')),
>>>>>>> 17d86b7 (creat model review)
]
