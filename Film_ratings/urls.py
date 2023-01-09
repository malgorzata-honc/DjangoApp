from django.urls import include, path
from rest_framework import routers 
from .views import ActorViewSet, DirectorViewSet, FilmViewSet, RatingViewSet


router = routers.DefaultRouter()
router.register(r'Actors', ActorViewSet)
router.register(r'Directors', DirectorViewSet)
router.register(r'Films', FilmViewSet)
router.register(r'Ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]