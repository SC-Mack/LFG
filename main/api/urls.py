from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from main.api import views as main_views

router = DefaultRouter()
router.register(r'reviews', main_views.ReviewViewSet)
router.register(r'profiles', main_views.CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]