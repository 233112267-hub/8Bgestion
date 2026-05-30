from django.urls import path

from .views import (
    index,
    registro_asesor,
    registro_asesorado,
    solicitudes,
    asesorias
)

urlpatterns = [

    # LOGIN
    path('', index, name='index'),

    # REGISTRO ASESOR
    path(
        'registro/asesor/',
        registro_asesor,
        name='registro_asesor'
    ),

    # REGISTRO ASESORADO
    path(
        'registro/asesorado/',
        registro_asesorado,
        name='registro_asesorado'
    ),

    path(
        'solicitudes/<int:id_asesor>/',
        solicitudes,
        name='solicitudes'
    ),
    path(
        'asesorias/<int:id_asesorado>/',
        asesorias,
        name='asesorias'
    ),

    path(
    'solicitar/<int:id_asesorado>/<int:id_asesor>/',
    solicitar_asesoria,
    name='solicitar_asesoria'
    ),

    path(
    'aceptar/<int:id_asesoria>/',
    aceptar_solicitud,
    name='aceptar_solicitud'
    ),

    path(
    'rechazar/<int:id_asesoria>/',
    rechazar_solicitud,
    name='rechazar_solicitud'
    ),
]