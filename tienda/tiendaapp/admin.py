
from django.contrib import admin
from tiendaapp.models import Producto
from tiendaapp.models import Vendedor


# Register your models here.

admin.site.register(Producto)
admin.site.register(Vendedor)

