from django import forms
from products.models import Products, Category

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['idproduct', 'name', 'price', 'category', 'product_picture']
        labels = { 'idproduct': ('Codigo del producto:' ), 'name': ('Nombre del producto'), 'price' : ('Precio:'), 'category' : ('Categoria del producto:'), 'product_picture' : ('Sube una foto:') }


class UpdateProducts (forms.ModelForm):
    class Meta: 
        model = Products
        fields = ['price', 'is_available']  

