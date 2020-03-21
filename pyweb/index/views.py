from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .handleLogin import *
from .handleSum import *
# Create your views here.

def index (request):

    return render(request, 'index/index.html')

def pin (request):
    return render(request, 'index/pin.html')

def withdrawal (request,userid):
    if request.method=="POST":
        checkUpdate=updateBalance(request,userid)
        if checkUpdate:
            message="Success!"

            return render(request,'index/test.html', { 'message':message,})
        else:

            message="Not enough funds! Please try again."
            return render(request, 'index/test.html', { 'message':message } )
    else:
        user=User.objects.get(id=userid)
        kartica=Kartica.objects.get(korisnik=user)
        return render(request, 'index/withdrawal.html',{'user':user,'kartica':kartica})
def test (request):
    if request.method=='POST':
        user=checkLogin(request)
        if user:
            return HttpResponseRedirect(reverse('withdrawal',args=(user.user_id,)))
        else:
            message="Nonexisting user! Try Again"
            return render(request,'index/test.html', { 'message':message})
    else:
        return render(request, 'index/test.html')
