from django.shortcuts import render

def index_view(request):
    return render(request, 'index-mainpage.html')

def form_view(request):
    return render(request, 'index-addpostpage.html')