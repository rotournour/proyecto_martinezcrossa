# Generated by Django 5.0.6 on 2024-06-08 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_idproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='idproduct',
            field=models.IntegerField(max_length=100, verbose_name='Codigo del producto'),
        ),
    ]
