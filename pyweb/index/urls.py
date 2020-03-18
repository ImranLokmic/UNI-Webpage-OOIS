from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pin/', views.pin, name='pin'),
    path('withdrawal/', views.withdrawal, name='withdrawal')
]
