from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('users/', include('users.urls')),
    path('manager/', include('hotels.urls')),
    path('reviews/', include('reviews.urls')),
    path('cal/', include('hotels.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
