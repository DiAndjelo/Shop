'''
Прыгаем во вьюху приложения магазина и в урл приложения продуктов
'''


from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('letmesee/', include('Products.urls')),

]