from django.db import models

# Create your models here.
class Tema(models.Model):
    nombre = models.CharField(max_length=255)
    dificultad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Asesor(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=255)
    nombre_usuario = models.CharField(max_length=255, unique=True)
    tarifa = models.FloatField()

    def __str__(self):
        return self.nombre


class Asesorado(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=255)
    nombre_usuario = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class TemasDelAsesor(models.Model):
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)


class Asesoria(models.Model):
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    asesorado = models.ForeignKey(Asesorado, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    confirmada = models.BooleanField(default=False)