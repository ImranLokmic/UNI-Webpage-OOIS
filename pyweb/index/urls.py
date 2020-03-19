from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('withdrawal/<int:userid>', views.withdrawal, name='withdrawal'),
    path('test/', views.test, name='test'),
]
