# Generated by Django 2.2.6 on 2019-11-27 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_productcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='product',
        ),
    ]
