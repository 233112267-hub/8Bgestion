from django.shortcuts import render
from .models import Asesor, Asesorado


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

        if asesor or asesorado:
            mensaje = "Login correcto"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render(request, 'index.html', {
        'mensaje': mensaje
    })