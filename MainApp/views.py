'''
Пока что просто рендер основной страницы сайта (Home)
Необходимо дополнить
'''

from django.shortcuts import render
from Products.models import *

def home(request):
    product_categories = ProductCategory.objects.all()
    leftbar_product = Product.objects.filter(mainapp_leftbar=True, is_active=True)
    topbar_products = Product.objects.filter(mainapp_topbar=True, is_active=True)
    midbar_products = Product.objects.filter(mainapp_midbar=True, is_active=True)
    botbar_products = Product.objects.filter(mainapp_botbar=True, is_active=True)
    product_images = ProductImage.objects.filter(is_main=True)
    product_categories = ProductCategory.objects.all()
    return render(request, 'main/home.html', locals())