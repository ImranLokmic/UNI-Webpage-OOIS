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
            message="Uspjeh"
            return render(request,'index/test.html',message)
        else:
            message="Neuspjeh unesite ponovo"
            return render(request, 'index/withdrawal.html', message)
    else:
        return render(request, 'index/withdrawal.html')
def test (request):
    if request.method=='POST':
        user=checkLogin(request)
        if user:
            return HttpResponseRedirect(reverse('withdrawal',args=(user.id,)))
        else:
            return render(request,'index/test.html')


    else:
        return render(request, 'index/test.html')
