from django import forms
from django.forms import ModelForm, Form 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from bugtracker.models import Ticket

class SignInForm(AuthenticationForm):
   username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
   password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'status', 
            'assigned_to'
        ]