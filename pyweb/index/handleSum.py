from .models import *


def updateBalance(request, userid):
    balans=request.POST['sum']
    balans=int(balans)
    user=User.objects.get(id=userid)
    kartica=Kartica.objects.get(korisnik=user)
    if(kartica.Balance>=balans):
        kartica.Balance=kartica.Balance-balans
        kartica.save()

        return True
    else:

        return False
