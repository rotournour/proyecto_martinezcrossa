
from django.urls import path
from products.views import product_detail, create_product, list_products, products_update, DeleteProducts

urlpatterns = [
     path('prueba/', product_detail, name='product_detail'),
     path('create/', create_product),
     path('list/', list_products, name='list_products'),
     path('update/<int:idproduct>/', products_update, ),
     path('delete/<int:idproduct>/', DeleteProducts.as_view(), name= 'delete')
]
