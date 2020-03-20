from django.urls import path
from . import views

urlpatterns = [
    path('withdrawal/<int:userid>', views.withdrawal, name='withdrawal'),
    path('', views.test, name='test'),
]
