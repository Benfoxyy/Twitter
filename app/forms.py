from django import forms
from .models import Twitt

class TwittForm(forms.ModelForm):
    class Meta:
        model = Twitt
        fields = ['auth','content']