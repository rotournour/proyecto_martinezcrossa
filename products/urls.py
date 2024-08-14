
from django.urls import path
from products.views import product_detail, create_product, list_products, UpdateProducts, DeleteProducts, product_details

urlpatterns = [
     path('prueba/', product_detail, name='product_detail'),
     path('create/', create_product),
     path('list/', list_products, name='list_products'),
     path('/<int:pk>/update/', UpdateProducts.as_view(), name= 'update'),
     path('/<int:pk>/delete/', DeleteProducts.as_view(), name= 'delete'),
     path('<int:idproduct>/', product_details, name='producto_detalle'),
]
