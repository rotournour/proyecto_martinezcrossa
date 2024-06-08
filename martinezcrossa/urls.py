
from django.contrib import admin
from django.urls import path,include
from martinezcrossa.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('products/', include('products.urls')),

]
