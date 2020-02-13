from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    prepopulated_fields = {'url': ('name',)}
    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductColor._meta.fields]

    class Meta:
        model = ProductColor

admin.site.register(ProductColor, ProductColorAdmin)

class ProductShippingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductShipping._meta.fields]
    list_editable = ('is_free', )

    class Meta:
        model = ProductShipping

admin.site.register(ProductShipping, ProductShippingAdmin)

class ProductAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'is_active', 'category', 'mini_description', 'price', 'is_new', 'mainapp_leftbar',
                    'mainapp_topbar', 'mainapp_midbar', 'mainapp_botbar', 'created', 'updated')
    inlines = [ProductImageInline]
    list_filter = ['is_active', 'is_new', 'created', 'updated']
    list_editable = ('is_active', 'price', 'is_new', 'mainapp_leftbar',
                    'mainapp_topbar', 'mainapp_midbar', 'mainapp_botbar')
    prepopulated_fields = {'url': ('name',)}
    summernote_fields = ('full_description', 'description', 'mini_description', 'full_specifiction')

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]
    list_editable = ('is_main',)
    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)