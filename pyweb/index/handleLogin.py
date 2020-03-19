from .models import Verifikacija



def checkLogin(request):
    kartica=request.POST['card']
    user=request.POST['own']
    pin=request.POST['p']

    User_kartica=Verifikacija.objects.filter(kartica=kartica)
    if User_kartica:
        return True
    else:
        return False
