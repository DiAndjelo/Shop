from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [

    path('', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),

]