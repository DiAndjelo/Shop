# Generated by Django 2.2.6 on 2019-10-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_productimage_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='static/img/products_images'),
        ),
    ]
