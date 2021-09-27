from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterUserForm, EventCreationForm
from .models import Event
# from json import loads # needed to convert string from database into json


def home(request):
    events = Event.objects.all()
    return render(request, 'orion/index.html', {'events': events})


def user_registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') # the parameter inside the redirect method takes a string of a Django 'urls.py' name
    else:
        form = RegisterUserForm()

    return render(request, 'orion/user_registration.html', {'form': form})


def create_new_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else: 
        form = EventCreationForm()

    return render(request, 'orion/create_new_event.html', {'form': form})


def blacklist(request):
    return render(request, 'orion/blacklist.html')


def edit_event(request):
    return render(request, 'orion/edit_event.html')


def edit_user(request):
    return render(request, 'orion/edit_user.html')


def my_events(request):
    return render(request, 'orion/my_events.html')


def events_registered_for(request):
    return render(request, 'orion/events_registered_for.html')