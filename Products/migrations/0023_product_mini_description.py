# Generated by Django 2.2.6 on 2019-12-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0022_product_full_specifiction'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mini_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
