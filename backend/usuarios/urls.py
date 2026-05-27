from django.urls import path

from .views import (
    index,
    registro_asesor,
    registro_asesorado,
    solicitudes
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

]