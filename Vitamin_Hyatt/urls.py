from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('manager/', include("hotels.urls")),
    path('users/', include('users.urls')),
=======
    path('users/', include('users.urls')),
    path('manager/', include("hotels.urls")),
>>>>>>> 0dcc30a (fix hetels.view)
]
