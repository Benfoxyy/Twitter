from django.shortcuts import render
from .models import Twitt

def index_view(request):
    twitts = Twitt.objects.filter(checked = True)
    return render(request, 'index-mainpage.html',{'twitts':twitts})

def form_view(request):
    return render(request, 'index-addpostpage.html')