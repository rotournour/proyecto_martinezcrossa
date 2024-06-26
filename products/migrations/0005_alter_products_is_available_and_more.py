# Generated by Django 5.0.6 on 2024-06-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_category_categories_alter_products_idproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='is_available',
            field=models.IntegerField(verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture',
            field=models.ImageField(blank=True, null=True, upload_to='products_images', verbose_name='Imagen del producto'),
        ),
    ]
