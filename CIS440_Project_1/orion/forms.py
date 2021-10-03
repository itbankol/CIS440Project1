from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Event


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class EventCreationForm(ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', 'date_of_event', 'author', 'attendees']
        widgets = {
            'author': forms.HiddenInput(),
            'attendees': forms.HiddenInput(),
            'date_of_event': DateTimeInput(),
        }
        