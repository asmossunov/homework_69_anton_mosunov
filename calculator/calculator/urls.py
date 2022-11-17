from django.contrib import admin
from django.urls import path
from core.views import add, subtract


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
]
