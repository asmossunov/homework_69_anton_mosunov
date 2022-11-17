from django.contrib import admin
from django.urls import path
from core.views import add, subtract, multiply, divide


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
]
