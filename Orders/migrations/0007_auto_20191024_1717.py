# Generated by Django 2.2.6 on 2019-10-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_auto_20191024_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Product status', 'verbose_name_plural': 'Product statuses'},
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Not available', 'Not available')], default='Available', max_length=24, null=True),
        ),
    ]
