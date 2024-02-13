from django.shortcuts import render,redirect
from .models import Twitt
from .forms import TwittForm

def index_view(request):
    if request.method == 'POST':
        form = TwittForm(request.POST or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.auth = request.user
            print('hello')
            obj.save()
            return redirect('/')
    twitts = Twitt.objects.filter(checked = True)
    form = TwittForm()
    return render(request, 'indexMane.html',{'twitts':twitts,'form':form})