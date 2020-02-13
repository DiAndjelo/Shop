# Generated by Django 2.2.6 on 2019-12-06 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0020_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Products.Product'),
        ),
    ]