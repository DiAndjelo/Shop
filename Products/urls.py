from django.contrib import admin
from django.urls import path

from Orders.urls import *
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product, name='product'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('basket_adding/', include('Orders.urls')),
]
