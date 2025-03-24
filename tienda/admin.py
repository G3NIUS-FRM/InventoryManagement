from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Categorias)
admin.site.register(Productos)
admin.site.register(PedidosParaTienda)
admin.site.register(DetallePedido)
admin.site.register(EntregasParaTienda)
