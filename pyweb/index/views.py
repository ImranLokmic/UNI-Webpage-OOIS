from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    return render(request, 'index/index.html')

def pin (request):
    return render(request, 'index/pin.html')

def withdrawal (request):
    return render(request, 'index/withdrawal.html')
