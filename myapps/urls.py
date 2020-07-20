from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('our_vision/', views.ourVisionView, name='our_vision'),
]
