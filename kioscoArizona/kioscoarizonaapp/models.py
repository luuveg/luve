from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    categoria= models.IntegerField()

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Categoria: {self.categoria}"

class Bebida(models.Model):
    congas = models.CharField(max_length=20)
    singas = models.CharField(max_length=20)
    sinazucar = models.CharField(max_length=20)

 def __str__(self) -> str:
        return f"Nombre: {self.nombre}