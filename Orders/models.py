from Products.models import Product
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from utils.main import disable_for_loaddata


class Status(models.Model):
    name = models.CharField("Name", max_length=24, blank=True, null=True, default=None)
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status %s" % self.name

    class Meta:
        verbose_name = 'Order status'
        verbose_name_plural = 'Order statuses'

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", blank=True, null=True, default=None, on_delete=models.CASCADE)
    total_amount = models.DecimalField("Total amount", default=0, max_digits=10, decimal_places=2)#total price for all products in order
    customer_name = models.CharField("Name", max_length=64, blank=False, null=True, default=None)
    customer_email = models.EmailField("Email", max_length=128, blank=True, null=True, default=None)
    customer_phone = models.CharField("Phone", max_length=48, blank=True, null=True, default=None)
    comments = models.TextField("Comments", blank=True, null=True, default=None)
    status = models.ForeignKey(Status, verbose_name="Status", null=True, on_delete = models.SET_NULL)
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order №%s " % (self.id)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name="Order",blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", blank=True, default=None, null=True, on_delete=models.SET_NULL)
    nmb = models.IntegerField("Quantity", default=1)
    price_per_item = models.DecimalField("Price per item", default=0, max_digits=10, decimal_places=2)
    total_price = models.DecimalField("Total price", default=0, max_digits=10, decimal_places=2)#price*nmb
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.product.name, self.product.price)

    class Meta:
        verbose_name = "Product in order"
        verbose_name_plural = "Products in order"

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item



        super(ProductInOrder, self).save(*args, **kwargs)

@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_amount = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField("Session key", max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, verbose_name="Order", blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", blank=True, default=None, null=True, on_delete=models.SET_NULL)
    nmb = models.IntegerField("Quantity", default=1)
    price_per_item = models.DecimalField("Price per item", default=0, max_digits=10, decimal_places=2)
    total_price = models.DecimalField("Total price", default=0, max_digits=10, decimal_places=2)#price*nmb
    is_active = models.BooleanField("Is it active product?", default=True)
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.product

    class Meta:
        verbose_name = "Product in basket"
        verbose_name_plural = "Products in basket"

    def save(self, *args, **kwargs):

        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item



        super(ProductInBasket, self).save(*args, **kwargs)