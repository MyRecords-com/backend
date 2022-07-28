from django.urls import path
from core_app.views import *
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

urlpatterns = [
    path('record/', RecordView.as_view(), name="records"),
    path('profile/', ProfileView.as_view(), name="profiles"),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('register/', views.EndPoint, name='register'),
    path('', views.getRoutes),
]