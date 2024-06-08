from itertools import product
from django.shortcuts import render
from .models import Products  # Asegúrate de importar tu modelo


def product_detail(request):
    products = Products.objects.all()
    return render(request, 'products/prueba.html', {'products': products})
