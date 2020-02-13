'''
Рендерим основную страницу магазина. Забираем с собой отфильтрованные по активности и главности(ВАЖНО!) картинки продуктов, а так же всех категорий для вывода.
В последствии создадим приложение категорий, откуда будем рендерить отдельные категории для каждого продукта.
'''

from django.shortcuts import render
from Products.models import *

def shop(request):
    product_images = ProductImage.objects.filter(is_main=True)
    product_categories = ProductCategory.objects.all()
    return render(request, 'shop/shop.html', locals())