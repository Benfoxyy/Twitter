from django import forms
from .models import Twitt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TwittForm(forms.ModelForm):
    class Meta:
        model = Twitt
        fields = ['auth','content']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password2']