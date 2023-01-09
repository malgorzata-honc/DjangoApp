from django.contrib import admin
from django.urls import include, path
from Film_ratings import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Film_ratings/', include('Film_ratings.urls')),
]