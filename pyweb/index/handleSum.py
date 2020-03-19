from .models import *


def updateBalance(request, userid):
    balans=request.POST['sum']
    user=User.objects.get(pk=userid)
    kartica=Kartica.objects.get(user=user)
    if(kartica.balans>=balans):
        kartica.balans=kartica.balans-balans
        kartica.save()

        return True
    else:

        return False
