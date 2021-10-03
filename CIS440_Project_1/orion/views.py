from django.shortcuts import render, redirect
# from django.contrib import messages
from .forms import RegisterUserForm, EventCreationForm
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    events = Event.objects.all()
    
    if request.method == 'POST':
        user = request.user
        event_obj = request.POST['event_object']
        for e in events:
            if str(e) == event_obj:
                e.attendees = e.attendees + f" {user.username}"
                e.save()
        return redirect('/')       
             
    return render(request, 'orion/index.html', {'events': events})


def user_registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/') # the parameter inside the redirect method takes a string of a Django 'urls.py' name
    else:
        form = RegisterUserForm()

    return render(request, 'orion/user_registration.html', {'form': form})


@login_required
def create_new_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else: 
        form = EventCreationForm()

    return render(request, 'orion/create_new_event.html', {'form': form})


@login_required
def edit_event(request):
    events = Event.objects.all()
    return render(request, 'orion/edit_event.html', {'events': events})


@login_required
def events_registered_for(request):
    events = Event.objects.all()
    return render(request, 'orion/events_registered_for.html', {'events': events})


@login_required
def sign_up_event(request):
    eventID = request.POST.get("event_object")
    event_to_register = Event.objects.get(id=eventID)
    return render(request, 'orion/user_sign_up.html', {'event': event_to_register, 'attendee': request.user})


@login_required()
def submit_sign_up(request):
    username = request.user.username
    eventID = request.POST.get("event_object")
    event_to_register = Event.objects.get(id=eventID)
    event_to_register.attendees += " " + username
    event_to_register.save()
    events = Event.objects.all()
    return render(request, 'orion/index.html', {'events': events})
