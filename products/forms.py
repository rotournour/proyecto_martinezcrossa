from django import forms
from products.models import Products, Category

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['idproduct', 'name', 'price', 'category', 'is_available', 'product_picture']
        labels = { 'idproduct': ('Codigo del producto:' ), 'name': ('Nombre del producto'), 'price' : ('Precio:'), 'category' : ('Categoria del producto:'), 'is_available' : ('Stock actual'), 'product_picture' : ('Sube una foto:') }

