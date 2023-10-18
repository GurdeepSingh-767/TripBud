from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'trip-images', TripPhotosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', CustomUserCreate, name='user_signup'),
    path('login/', CustomUserLogin, name='user_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create-checkout-session/<int:trip_id>/', views.create_checkout_session, name='create-checkout-session'),
]
