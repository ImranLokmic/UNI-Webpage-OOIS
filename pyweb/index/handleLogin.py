from .models import Verifikacija



def checkLogin(request):
    kartica=request.POST['card']
    user=request.POST['own']
    pin=request.POST['p']

    User_kartica=Verifikacija.objects.get(kartica=kartica)

    return User_kartica
