from django.urls import path

from .views import (
    index,
    registro_asesor,
    registro_asesorado
)
from .views import api_asesores, api_asesorias, api_solicitudes

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

        # API endpoints
        path('api/asesores/', api_asesores, name='api_asesores'),
        path('api/asesorias/', api_asesorias, name='api_asesorias'),
        path('api/solicitudes/', api_solicitudes, name='api_solicitudes'),

]