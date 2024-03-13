from django.shortcuts import render,redirect
from .models import Twitt
from .forms import TwittForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate

@login_required(login_url='login')
def index_view(request):
    if request.method == 'POST':
        form = TwittForm(request.POST or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.auth = request.user
            obj.save()
            return redirect('/')
    twitts = Twitt.objects.filter(checked = True)
    form = TwittForm()
    return render(request, 'indexMane.html',{'twitts':twitts,'form':form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/')
    else:
        form = RegistrationForm()



    return render(request,'registration/sign_up.html',{'form':form})