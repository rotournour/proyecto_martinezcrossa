
from django.urls import path
from products.views import my_view

urlpatterns = [
     path ('prueba/', my_view),
]
