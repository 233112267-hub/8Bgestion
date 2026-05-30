from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Asesor,
    Asesorado,
    Asesoria,
    Horario
)


# =========================================
# LOGIN
# =========================================

def index(request):

    mensaje = ""

    if request.method == "POST":

        usuario = request.POST.get("usuario")
        password = request.POST.get("password")

        # -----------------------------
        # LOGIN ASESOR
        # -----------------------------

        asesor = Asesor.objects.filter(
            nombre_usuario=usuario,
            contrasenia=password
        ).first()

        if not asesor:

            asesor = Asesor.objects.filter(
                email=usuario,
                contrasenia=password
            ).first()

        # -----------------------------
        # LOGIN ASESORADO
        # -----------------------------

        asesorado = Asesorado.objects.filter(
            nombre_usuario=usuario,
            contrasenia=password
        ).first()

        if not asesorado:

            asesorado = Asesorado.objects.filter(
                email=usuario,
                contrasenia=password
            ).first()

        # -----------------------------
        # REDIRECCIONES
        # -----------------------------

        if asesor:

            return redirect(
                'solicitudes',
                id_asesor=asesor.id_asesor
            )

        elif asesorado:

            return redirect(
                'asesorias',
                id_asesorado=asesorado.id_asesorado
            )

        else:

            mensaje = "Usuario o contraseña incorrectos"

    return render(
        request,
        'index.html',
        {
            'mensaje': mensaje
        }
    )


# =========================================
# REGISTRO ASESOR
# =========================================

def registro_asesor(request):

    mensaje = ""

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        tarifa = request.POST.get("tarifa")

        if password != confirm_password:

            mensaje = "Las contraseñas no coinciden"

        elif Asesor.objects.filter(
            nombre_usuario=usuario
        ).exists():

            mensaje = "El usuario ya existe"

        elif Asesor.objects.filter(
            email=email
        ).exists():

            mensaje = "El correo ya existe"

        else:

            Asesor.objects.create(
                nombre=nombre,
                email=email,
                nombre_usuario=usuario,
                contrasenia=password,
                tarifa=tarifa,
                disponibilidad=True
            )

            mensaje = "Asesor registrado correctamente"

    return render(
        request,
        'registro_asesor.html',
        {
            'mensaje': mensaje
        }
    )


# =========================================
# REGISTRO ASESORADO
# =========================================

def registro_asesorado(request):

    mensaje = ""

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            mensaje = "Las contraseñas no coinciden"

        elif Asesorado.objects.filter(
            nombre_usuario=usuario
        ).exists():

            mensaje = "El usuario ya existe"

        elif Asesorado.objects.filter(
            email=email
        ).exists():

            mensaje = "El correo ya existe"

        else:

            Asesorado.objects.create(
                nombre=nombre,
                email=email,
                nombre_usuario=usuario,
                contrasenia=password
            )

            mensaje = "Asesorado registrado correctamente"

    return render(
        request,
        'registro_asesorado.html',
        {
            'mensaje': mensaje
        }
    )


# =========================================
# PANEL DEL ASESOR
# =========================================

def solicitudes(request, id_asesor):

    asesor = get_object_or_404(
        Asesor,
        id_asesor=id_asesor
    )

    solicitudes = Asesoria.objects.filter(
        asesor=asesor
    ).order_by('-id_asesoria')

    return render(
        request,
        'solicitudes.html',
        {
            'asesor': asesor,
            'solicitudes': solicitudes
        }
    )


# =========================================
# PANEL DEL ASESORADO
# =========================================

def asesorias(request, id_asesorado):

    asesorado = get_object_or_404(
        Asesorado,
        id_asesorado=id_asesorado
    )

    asesores = Asesor.objects.all()

    mis_asesorias = Asesoria.objects.filter(
        asesorado=asesorado
    ).order_by('-id_asesoria')

    return render(
        request,
        'asesorias.html',
        {
            'asesorado': asesorado,
            'asesores': asesores,
            'mis_asesorias': mis_asesorias
        }
    )


# =========================================
# CREAR SOLICITUD
# =========================================

def solicitar_asesoria(
    request,
    id_asesorado,
    id_asesor
):

    asesorado = get_object_or_404(
        Asesorado,
        id_asesorado=id_asesorado
    )

    asesor = get_object_or_404(
        Asesor,
        id_asesor=id_asesor
    )

    Asesoria.objects.create(
        asesor=asesor,
        asesorado=asesorado,
        estado='Pendiente',
        tipo='Individual',
        comentario='Solicitud enviada'
    )

    return redirect(
        'asesorias',
        id_asesorado=id_asesorado
    )


# =========================================
# ACEPTAR SOLICITUD
# =========================================

def aceptar_solicitud(
    request,
    id_asesoria
):

    asesoria = get_object_or_404(
        Asesoria,
        id_asesoria=id_asesoria
    )

    asesoria.estado = "Aceptada"
    asesoria.save()

    return redirect(
        'solicitudes',
        id_asesor=asesoria.asesor.id_asesor
    )


# =========================================
# RECHAZAR SOLICITUD
# =========================================

def rechazar_solicitud(
    request,
    id_asesoria
):

    asesoria = get_object_or_404(
        Asesoria,
        id_asesoria=id_asesoria
    )

    asesoria.estado = "Rechazada"
    asesoria.save()

    return redirect(
        'solicitudes',
        id_asesor=asesoria.asesor.id_asesor
    )