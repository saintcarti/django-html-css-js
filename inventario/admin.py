from django.contrib import admin
from .models import Categoria,Marca,Camara ,Boleta,DetalleBoleta
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['idCategoria', 'nombreCategoria']

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['idMarca', 'nombreMarca']

@admin.register(Camara)
class CamaraAdmin(admin.ModelAdmin):
    list_display = ['idCamara', 'nombreCamara', 'precio', 'descripcion', 'categoria', 'marca', 'imagen', 'stock']

@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    list_display = ['id_boleta', 'total', 'fechaCompra', 'usuario']

@admin.register(DetalleBoleta)
class DetalleBoletaAdmin(admin.ModelAdmin):
    list_display = ['id_boleta', 'id_detalle_boleta', 'id_producto', 'cantidad', 'subtotal']