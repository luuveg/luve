from django.contrib import admin
from .models import Producto, Bebida, Golosina, Snacks


# Register your models here.

admin.site.register(Producto)
admin.site.register(Bebida)
admin.site.register(Golosina)
admin.site.register(Snacks)