from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='orion-home'),
    path('create-user/', views.create_user, name='orion-create-user')
]