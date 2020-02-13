'''
Урл Home-приложения. Отсюда переход во вьюху с Home страницей и в урл приложения магазина.
'''


from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', include('ShopApp.urls')),
]
