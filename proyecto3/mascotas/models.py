from django.db import models

class Responsable(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.CharField(max_length=150, unique=True)
    rut = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=150)
    anio_nacimiento = models.IntegerField()
    especie = models.CharField(max_length=100)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return self.nombre