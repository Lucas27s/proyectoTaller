from django.urls import path
from .views import *


urlpatterns = [
    path('home/', home, name='home'),
    path('', home, name='home'),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact'),
    path('agregar/', agregar_atencion, name='agregar_atencion'),
    path('listar/', listar_atencion, name='listar_atencion'),
    path('mostrar/', mostrar_atenciones, name='mostrar_atenciones'),
    path('modificar/<diagnostico>/', modificar_atencion, name='modificar_atencion'),
    path('eliminar_atencion/<diagnostico>/', eliminar_atencion, name='eliminar_atencion'),
    path('login_usuario/', login_usuario, name='login_usuario'),
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    path('listar_mecanico/', listar_mecanico, name='listar_mecanico'),
    path('eliminar_mecanico/<rut>/', eliminar_mecanico, name='eliminar_mecanico'),
    path('modificar_mecanico/<rut>/', modificar_mecanico, name='modificar_mecanico'),
    path('agregar_mecanico/', agregar_mecanico, name='agregar_mecanico'), 
    path('agregar_categoria/', agregar_categoria, name='agregar_categoria'),
    path('postulacion/', postulacion, name='postulacion'),
    path('listar_postulacion/', listar_postulacion, name='listar_postulacion'),
    path('detalle/<pk>/', detalle_atencion, name='detalle_atencion'),
    path('detalle_postulante/<pk>/', detalle_postulante, name='detalle_postulante'),
    
]