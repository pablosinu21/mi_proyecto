from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_vencimiento = models.DateField()

    class Meta:
        db_table = 'producto'  # Esto cambia el nombre de la tabla en la BD

    def __str__(self):
        return self.nombre

