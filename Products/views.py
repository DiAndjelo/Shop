from django.shortcuts import render, redirect
from .models import *
from django.views.generic.base import View
from Orders.urls import *
from .forms import ReviewForm
# Create your views here.

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    product_categories = ProductCategory.objects.all()

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    #app_name = "Orders"
    product_images = ProductImage.objects.filter(product=product)
    slug_field = 'url'
    return render(request, 'products/product.html', locals())

def category(request, category_name):
    product_categories = ProductCategory.objects.all()
    category = ProductCategory.objects.get(name=category_name)
    products = Product.objects.filter(category=category, is_active=True)
    product_images = ProductImage.objects.filter(product__category=category, is_main=True)

    return render(request, 'categories/category.html', locals())

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product_id = pk
            form.save()
        return redirect(product.get_absolute_url())