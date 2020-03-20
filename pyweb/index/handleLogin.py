from .models import Verifikacija



def checkLogin(request):
    kartica=request.POST['card']
    user=request.POST['own']
    pin=request.POST['p']
    User_kartica=""

    try:

        User_kartica=Verifikacija.objects.get(kartica=kartica,pin=pin)

    except:
        print("nepostojeci korisnik")
    return User_kartica
