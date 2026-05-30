from django.db import models


# =====================================
# TEMA
# =====================================

class Tema(models.Model):

    id_tema = models.AutoField(primary_key=True)

    nombre = models.CharField(
        max_length=255
    )

    dificultad = models.IntegerField()

    class Meta:
        db_table = 'TEMA'

    def __str__(self):
        return self.nombre


# =====================================
# ASESOR
# =====================================

class Asesor(models.Model):

    id_asesor = models.AutoField(
        primary_key=True
    )

    nombre = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        unique=True
    )

    contrasenia = models.CharField(
        max_length=255
    )

    nombre_usuario = models.CharField(
        max_length=255,
        unique=True
    )

    tarifa = models.FloatField()

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    modalidad = models.CharField(
        max_length=20,
        choices=[
            ('Individual', 'Individual'),
            ('Grupal', 'Grupal')
        ],
        default='Individual'
    )

    promedio_calificacion = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0
    )

    disponibilidad = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = 'ASESOR'

    def __str__(self):
        return self.nombre


# =====================================
# ASESORADO
# =====================================

class Asesorado(models.Model):

    id_asesorado = models.AutoField(
        primary_key=True
    )

    nombre = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        unique=True
    )

    contrasenia = models.CharField(
        max_length=255
    )

    nombre_usuario = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        db_table = 'ASESORADO'

    def __str__(self):
        return self.nombre


# =====================================
# TEMAS DEL ASESOR
# =====================================

class TemasDelAsesor(models.Model):

    asesor = models.ForeignKey(
        Asesor,
        on_delete=models.CASCADE
    )

    tema = models.ForeignKey(
        Tema,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'TEMASDELASESOR'


# =====================================
# HORARIOS
# =====================================

class Horario(models.Model):

    id_horario = models.AutoField(
        primary_key=True
    )

    asesor = models.ForeignKey(
        Asesor,
        on_delete=models.CASCADE
    )

    dia_semana = models.CharField(
        max_length=20
    )

    hora_inicio = models.TimeField()

    hora_fin = models.TimeField()

    disponible = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = 'HORARIO'

    def __str__(self):

        return (
            f"{self.asesor.nombre} - "
            f"{self.dia_semana} "
            f"{self.hora_inicio}"
        )


# =====================================
# ASESORIAS
# =====================================

class Asesoria(models.Model):

    id_asesoria = models.AutoField(
        primary_key=True
    )

    asesor = models.ForeignKey(
        Asesor,
        on_delete=models.CASCADE
    )

    asesorado = models.ForeignKey(
        Asesorado,
        on_delete=models.CASCADE
    )

    horario = models.ForeignKey(
        Horario,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    tipo = models.CharField(
        max_length=20,
        choices=[
            ('Individual', 'Individual'),
            ('Grupal', 'Grupal')
        ],
        default='Individual'
    )

    estado = models.CharField(
        max_length=20,
        choices=[
            ('Pendiente', 'Pendiente'),
            ('Aceptada', 'Aceptada'),
            ('Rechazada', 'Rechazada'),
            ('Finalizada', 'Finalizada')
        ],
        default='Pendiente'
    )

    comentario = models.TextField(
        blank=True,
        null=True
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = 'ASESORIA'


# =====================================
# CALIFICACIONES
# =====================================

class Calificacion(models.Model):

    id_calificacion = models.AutoField(
        primary_key=True
    )

    asesoria = models.ForeignKey(
        Asesoria,
        on_delete=models.CASCADE
    )

    puntuacion = models.IntegerField()

    comentario = models.TextField()

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = 'CALIFICACION'


# =====================================
# NOTIFICACIONES
# =====================================

class Notificacion(models.Model):

    id_notificacion = models.AutoField(
        primary_key=True
    )

    asesor = models.ForeignKey(
        Asesor,
        on_delete=models.CASCADE
    )

    mensaje = models.TextField()

    leida = models.BooleanField(
        default=False
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = 'NOTIFICACION'


# =====================================
# GRUPOS DE ASESORIA
# =====================================

class GrupoAsesoria(models.Model):

    id_grupo = models.AutoField(
        primary_key=True
    )

    asesoria = models.OneToOneField(
        Asesoria,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'GRUPO_ASESORIA'


# =====================================
# INTEGRANTES DEL GRUPO
# =====================================

class IntegranteGrupo(models.Model):

    id_integrante = models.AutoField(
        primary_key=True
    )

    grupo = models.ForeignKey(
        GrupoAsesoria,
        on_delete=models.CASCADE
    )

    asesorado = models.ForeignKey(
        Asesorado,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'INTEGRANTE_GRUPO'