from django.db import models


#
class Proveedor(models.Model):

    razon_social = models.CharField(max_length=50)
    cuit = models.IntegerField()
    celular = models.IntegerField()

    def __str__(self):
        return f"{self.razon_social}"


class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"
