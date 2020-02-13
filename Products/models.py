from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    """Категории продуктов"""
    #product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT)
    name = models.CharField("Category", max_length=64)
    url = models.SlugField(max_length=256, unique=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

class ProductColor(models.Model):
    """Цвета продуктов"""
    color = models.CharField("Color", max_length=32)
    image = models.ImageField("Color image", upload_to="colors/")

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Product Color"
        verbose_name_plural = "Product Colors"

class ProductShipping(models.Model):
    """Доставка продукта"""
    is_free = models.BooleanField("Is it free shipping?", default=False)
    name = models.CharField("Name", max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Shipping"
        verbose_name_plural = "Product Shippings"

class Product(models.Model):
    """Продукт"""
    name = models.CharField("Name", max_length=128)
    category = models.ForeignKey(ProductCategory, verbose_name="Categories", null=True, on_delete=models.SET_NULL)
    price = models.DecimalField("Price", default=0, max_digits=10, decimal_places=2)
    is_active = models.BooleanField("Is it active product?", default=True)
    is_new = models.BooleanField("Is it new product?", default=False)
    colors = models.ManyToManyField(ProductColor, verbose_name="Product colors")
    shippings = models.ManyToManyField(ProductShipping, verbose_name="Product shippings")
    year = models.PositiveSmallIntegerField("Release date", default=2020    )
    mainapp_leftbar = models.BooleanField("Put this product on homepage leftbar(max 1 product)?", default=False)
    mainapp_topbar = models.BooleanField("Put this product on homepage topbar(max 8 product)?", default=False)
    mainapp_midbar = models.BooleanField("Put this product on homepage midbar(max 3 product)?", default=False)
    mainapp_botbar = models.BooleanField("Put this product on homepage botbar(max 8 product)?", default=False)
    mini_description = models.TextField("Homepage description", blank=True, null=True)
    description = models.TextField("Shoppage description", blank=True, null=True)
    full_description = models.TextField("Productpage description", blank=True, null=True)
    full_specifiction = models.TextField("Specifiction", blank=True, null=True)
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)
    url = models.SlugField(max_length=256, unique=True, default='')

    def get_absolute_url(self):
        return "/shop/letmesee/product/%i/" % self.id

    def __str__(self):
        return "%s, $%s " % (self.name, self.price)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class ProductImage(models.Model):
    """Изображения продукта"""
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    image = models.ImageField("Image", upload_to='products_images/')
    is_main = models.BooleanField("Is it main image?", default=False)

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.PositiveSmallIntegerField("Value", default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Rating Star"
        verbose_name_plural = "Rating Stars"

class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP adress", max_length=16)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Star")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=64)
    prons = models.TextField("Prons", max_length=4096)
    cons = models.TextField("Cons", max_length=4096)
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"




