from django.shortcuts import render
from .models import Products  # Asegúrate de importar tu modelo

def my_view(request):
    # Obtén todos los objetos de tu modelo
    items = Products.objects.all()
    # Pasa los objetos al contexto de la plantilla
    return render(request, 'products/prueba.html', {'items': items, 'qr_code': img_str})


