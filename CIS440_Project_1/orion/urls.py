from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='orion/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='orion/logout.html'), name='logout'),
    path('', views.home, name='home'),
    path('user-registration/', views.user_registration, name='user-registration'),
    path('create-new-event/', views.create_new_event, name='create-new-event'),
    path('edit-event/', views.edit_event, name='edit-event'),
    path('events-registered-for', views.events_registered_for, name='events-registered-for'),
]