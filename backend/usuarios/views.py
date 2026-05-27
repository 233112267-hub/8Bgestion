from django.shortcuts import render, redirect
from .models import Asesor, Asesorado
from .models import Asesoria


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

            return redirect(
                'solicitudes',
                id_asesor=asesor.id_asesor
          )

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

def solicitudes(request, id_asesor):

    asesor = Asesor.objects.get(
        id_asesor=id_asesor
    )

    solicitudes = Asesoria.objects.filter(
        asesor=asesor
    )

    return render(request, 'solicitudes.html', {

        'asesor': asesor,
        'solicitudes': solicitudes

    })