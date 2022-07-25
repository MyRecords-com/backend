from django.urls import path
from core_app.views import *
# from . import views

urlpatterns = [
    path('record/', RecordView.as_view(), name="records"),
    path('profile/', ProfileView.as_view(), name="profiles"),
]