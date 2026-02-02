"""
URLs para la aplicación CV
"""

from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    # Vista principal
    path('', views.index, name='index'),
    
    # Vista de impresión
    path('print-preview/', views.print_preview, name='print_preview'),
    
    # Rutas protegidas para servir archivos
    path('protected/perfil/<int:perfil_id>/foto/', views.servir_foto, name='servir_foto'),
    path('protected/experiencia/<int:experiencia_id>/rutacertificado/', views.servir_certificado_experiencia, name='servir_certificado_experiencia'),
    path('protected/curso/<int:curso_id>/rutacertificado/', views.servir_certificado_curso, name='servir_certificado_curso'),
    path('protected/reconocimiento/<int:reconocimiento_id>/rutacertificado/', views.servir_certificado_reconocimiento, name='servir_certificado_reconocimiento'),
]
