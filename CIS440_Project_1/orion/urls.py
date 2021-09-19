from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='orion-home'),
    path('user-registration/', views.user_registration, name='orion-user-registration')
]