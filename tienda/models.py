from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()
    def __str__(self):
        return self.nombre
    


class Productos(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    categoria=models.ForeignKey(Categorias, on_delete=models.CASCADE)
    fecha_de_ingreso=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre
class PedidosParaTienda(models.Model):
    surtidor=models.CharField(max_length=100)
    productos = models.ManyToManyField(Productos, through="DetallePedido")
    fecha=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.surtidor} - {self.fecha}"
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(PedidosParaTienda, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.pedido} - {self.producto}"
class EntregasParaTienda(models.Model):
    pedido=models.ForeignKey(PedidosParaTienda, on_delete=models.CASCADE)
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE) 
    cantidad=models.IntegerField()
    fecha_de_ingreso=models.DateField(auto_now_add=True)
    fecha_de_caducidad=models.DateField()
    def __str__(self):
        return f"{self.producto} - {self.cantidad}"