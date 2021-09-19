from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'orion/index.html')


def create_user(request):
    return render(request, 'orion/create_user.html')
