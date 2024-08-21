from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from django.urls import reverse
from django.conf import settings



class Category (models.Model):
    categories = models.CharField(max_length=100, null=True, verbose_name= "Categoria del producto")
    

    
    def __str__(self):
        return self.categories
    
    
    class Meta():
        db_table = "Categories"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['categories'] 


class Products (models.Model):
    idproduct = models.IntegerField(verbose_name= "Codigo del producto")
    name = models.CharField(max_length=100, verbose_name= "Nombre del producto")
    price = models.FloatField(verbose_name= "Precio del producto")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name= "Categoria del producto")
    is_available = models.IntegerField(verbose_name= "Stock")
    product_picture = models.ImageField(upload_to='products_images', null=True, blank=True, verbose_name= "Imagen del producto")
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
    
    class Meta():
        db_table = "Products"
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} con codigo {self.idproduct} de de la categoria {self.category} con un precio de {self.price}'
    

    def get_absolute_url(self):
        return reverse('producto_detalle', kwargs={'idproduct': self.idproduct})

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # Obtener el dominio completo
                # Detectar si estás en un entorno local
        if settings.DEBUG:
            # Para desarrollo local
            domain = 'http://localhost:8000'
        else:
            # Para producción
            domain = settings.SITE_URL
        
        full_url = f'{domain}{self.get_absolute_url()}'
        qr.add_data(full_url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f'qr_{self.idproduct}.png'
        self.qr_code.save(file_name, File(buffer), save=False)

        super().save(*args, **kwargs)

    class Meta:
        db_table = "Products"
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} con codigo {self.idproduct} de la categoria {self.category} con un precio de {self.price}'