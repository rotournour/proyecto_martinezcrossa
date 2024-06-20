from django.contrib import admin
from django.urls import path,include
from martinezcrossa import settings
from martinezcrossa.views import index
from martinezcrossa.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', index, name='index'),]
    #path('users/', include('users.urls'))] + static(MEDIA_URL, document_root = MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  