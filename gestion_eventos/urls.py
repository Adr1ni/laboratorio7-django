from django.contrib import admin
from django.urls import path
from gestion_eventos import views

urlpatterns = [
    path('', views.inicio,name='incio'),

    path('usuarios/', views.usuarios,name='usuarios'),
    path('crear_usuario/', views.crearUsuario,name='crear_usuario'),
    path('actualizar_usuarios/<int:usuario_id>/', views.editarUsuario,name='actualizar_usuario'),
    path('eliminar_usuarios/<int:usuario_id>/', views.eliminarUsuario,name='eliminar_usuario'),

    path('eventos/', views.eventos,name='eventos'),
    path('crear_evento/', views.crearEvento,name='crear_evento'),
    path('actualizar_evento/<int:evento_id>/', views.editarEvento,name='actualizar_evento'),
    path('eliminar_evento/<int:evento_id>/', views.eliminarEvento,name='eliminar_evento'),

    path('registros/', views.registros,name='registros'),
    path('crear_registro/', views.crearRegistro,name='crear_registro'),
    path('actualizar_registro/<int:registro_id>/', views.editarRegistro,name='actualizar_registro'),
    path('eliminar_registro/<int:registro_id>/', views.eliminarRegistro,name='eliminar_registro'),
]