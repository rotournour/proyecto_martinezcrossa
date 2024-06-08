from django.contrib import admin
from products.models import Products, Category


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    search_fields = ('category',)
    list_filter = ('is_available',)
    
    
@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('categories',)

