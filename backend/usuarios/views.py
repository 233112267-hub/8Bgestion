from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Asesor, Asesorado, TemasDelAsesor, Asesoria
from django.utils.dateformat import format as django_date_format


def index(request):

    mensaje = ""

    if request.method == "POST":

        usuario = request.POST.get("usuario")
        password = request.POST.get("password")

        asesor = Asesor.objects.filter(
            nombre_usuario=usuario,
            contrasenia=password
        ).first()

        asesorado = Asesorado.objects.filter(
            nombre_usuario=usuario,
            contrasenia=password
        ).first()

        if asesor:

            return render(request, 'solicitudes.html', {
            'asesor': asesor
            })

        elif asesorado:

            asesores = Asesor.objects.all()

            return render(request, 'asesorias.html', {
                'asesorado': asesorado,
                'asesores': asesores
    })
        else:

            mensaje = "Usuario o contraseña incorrectos"

    return render(request, 'index.html', {
        'mensaje': mensaje
    })


# -----------------------------------
# REGISTRO ASESOR
# -----------------------------------

def registro_asesor(request):

    mensaje = ""

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")
        tarifa = request.POST.get("tarifa")

        existe = Asesor.objects.filter(
            nombre_usuario=usuario
        ).exists()

        if existe:

            mensaje = "El usuario ya existe"

        else:

            Asesor.objects.create(
                nombre=nombre,
                email=email,
                nombre_usuario=usuario,
                contrasenia=password,
                tarifa=tarifa
            )

            mensaje = "Asesor registrado correctamente"

    return render(request, 'registro_asesor.html', {
        'mensaje': mensaje
    })


# -----------------------------------
# REGISTRO ASESORADO
# -----------------------------------

def registro_asesorado(request):

    mensaje = ""

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")

        existe = Asesorado.objects.filter(
            nombre_usuario=usuario
        ).exists()

        if existe:

            mensaje = "El usuario ya existe"

        else:

            Asesorado.objects.create(
                nombre=nombre,
                email=email,
                nombre_usuario=usuario,
                contrasenia=password
            )

            mensaje = "Asesorado registrado correctamente"

    return render(request, 'registro_asesorado.html', {
        'mensaje': mensaje
    })


def api_asesores(request):
    asesores = Asesor.objects.all()
    data = []
    for a in asesores:
        tema_rel = TemasDelAsesor.objects.filter(asesor=a).select_related('tema').first()
        materia = tema_rel.tema.nombre if tema_rel else ''
        data.append({
            'id': a.id_asesor,
            'nombre': a.nombre,
            'materia': materia,
            'profesor': a.nombre,
            'tarifa': a.tarifa
        })
    return JsonResponse({'asesores': data})


def api_asesorias(request):
    asesorias = Asesoria.objects.select_related('asesor', 'asesorado').all()
    data = []
    for asr in asesorias:
        tema_rel = TemasDelAsesor.objects.filter(asesor=asr.asesor).select_related('tema').first()
        materia = tema_rel.tema.nombre if tema_rel else ''
        hora = asr.fecha.strftime('%I:%M %p') if asr.fecha else ''
        data.append({
            'id': asr.pk,
            'asesor_nombre': asr.asesor.nombre,
            'asesorado_nombre': asr.asesorado.nombre,
            'materia': materia,
            'fecha': asr.fecha.isoformat() if asr.fecha else None,
            'hora': hora,
            'confirmada': asr.confirmada
        })
    return JsonResponse({'asesorias': data})


def api_solicitudes(request):
    solicitudes = Asesoria.objects.select_related('asesor', 'asesorado').all()
    data = []
    for s in solicitudes:
        tema_rel = TemasDelAsesor.objects.filter(asesor=s.asesor).select_related('tema').first()
        materia = tema_rel.tema.nombre if tema_rel else ''
        hora = s.fecha.strftime('%I:%M %p') if s.fecha else ''
        estado = 'Aprobada' if s.confirmada else 'Pendiente'
        data.append({
            'id': s.pk,
            'alumno': s.asesorado.nombre,
            'materia': materia,
            'estado': estado,
            'hora': hora
        })
    return JsonResponse({'solicitudes': data})