from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-registration/', views.user_registration, name='user-registration'),
    path('create-new-event/', views.create_new_event, name='create-new-event'),
    path('blacklist/', views.blacklist, name='blacklist'),
    path('edit-event/', views.edit_event, name='edit-event'),
    path('edit-user/', views.edit_user, name='edit-user'),
]