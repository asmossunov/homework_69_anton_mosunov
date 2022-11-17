from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from calculator.views import add, subtract, multiply, divide
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
    path('', include('webapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
