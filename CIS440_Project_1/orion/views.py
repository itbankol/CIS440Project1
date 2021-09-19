from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterUserForm

def home(request):
    return render(request, 'orion/index.html')


def user_registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') # the parameter inside the redirect method takes a string of a Django 'views' name
    else:
        form = RegisterUserForm()

    return render(request, 'orion/user_registration.html', {'form': form})
