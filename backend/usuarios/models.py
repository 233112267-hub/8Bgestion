from django.db import models


class Tema(models.Model):

    id_tema = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    dificultad = models.IntegerField()

    class Meta:
        db_table = 'TEMA'

    def __str__(self):
        return self.nombre


class Asesor(models.Model):

    id_asesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=255)
    nombre_usuario = models.CharField(max_length=255, unique=True)
    tarifa = models.FloatField()

    class Meta:
        db_table = 'ASESOR'

    def __str__(self):
        return self.nombre


class Asesorado(models.Model):

    id_asesorado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=255)
    nombre_usuario = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'ASESORADO'

    def __str__(self):
        return self.nombre


class TemasDelAsesor(models.Model):

    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TEMASDELASESOR'


class Asesoria(models.Model):

    id_asesoria = models.AutoField(
        primary_key=True
    )

    asesor = models.ForeignKey(
        Asesor,
        on_delete=models.CASCADE,
        db_column='id_asesor'
    )

    asesorado = models.ForeignKey(
        Asesorado,
        on_delete=models.CASCADE,
        db_column='id_asesorado'
    )

    fecha = models.DateTimeField()

    estado = models.CharField(
        max_length=50,
        default='Pendiente'
    )


    class Meta:
        db_table = 'ASESORIA'