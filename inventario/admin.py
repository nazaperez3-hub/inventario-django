from django.contrib import admin
from .models import Producto, Movimiento
from django.utils.html import format_html


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mostrar_imagen', 'stock', 'costo_unitario', 'precio_venta')
    search_fields = ('nombre',)
    list_filter = ('precio_venta',)

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.imagen.url)
        return "Sin imagen"

    mostrar_imagen.short_description = "Imagen"


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Movimiento)
