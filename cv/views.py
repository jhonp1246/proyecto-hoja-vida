"""
Vistas para la aplicación CV
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string
from django.conf import settings
from .models import Perfil
import os


def index(request):
    """Vista principal - muestra el CV del perfil activo"""
    
    # Obtener el perfil activo (el primero)
    perfil = Perfil.objects.filter(activo=True).first()
    
    if not perfil:
        return render(request, 'cv/no_perfil.html')
    
    # Obtener todas las secciones con ordenamiento cronológico correcto
    experiencias = perfil.experiencias.all().order_by('-fecha_inicio')
    cursos = perfil.cursos.all().order_by('-fecha_inicio')
    reconocimientos = perfil.reconocimientos.all().order_by('-fecha')
    productos_academicos = perfil.productos_academicos.all().order_by('-fecha')
    productos_laborales = perfil.productos_laborales.all().order_by('-fecha')
    
    context = {
        'perfil': perfil,
        'experiencias': experiencias if perfil.mostrar_experiencia else [],
        'cursos': cursos if perfil.mostrar_cursos else [],
        'reconocimientos': reconocimientos if perfil.mostrar_reconocimientos else [],
        'productos_academicos': productos_academicos if perfil.mostrar_productos_academicos else [],
        'productos_laborales': productos_laborales if perfil.mostrar_productos_laborales else [],
        'user': request.user,
    }
    
    return render(request, 'cv/index.html', context)


def print_preview(request):
    """Vista para previsualización de impresión con filtros de secciones"""
    
    perfil = Perfil.objects.filter(activo=True).first()
    
    if not perfil:
        return render(request, 'cv/no_perfil.html')
    
    # Obtener filtros de secciones desde la URL
    mostrar_datos_personales = request.GET.get('datos-personales', '1') == '1'
    mostrar_experiencia = request.GET.get('experiencia', '1') == '1'
    mostrar_cursos = request.GET.get('cursos', '1') == '1'
    mostrar_reconocimientos = request.GET.get('reconocimientos', '1') == '1'
    mostrar_productos_academicos = request.GET.get('productos-academicos', '1') == '1'
    mostrar_productos_laborales = request.GET.get('productos-laborales', '1') == '1'
    
    # Obtener datos según filtros
    context = {
        'perfil': perfil if mostrar_datos_personales else None,
        'experiencias': perfil.experiencias.all().order_by('-fecha_inicio') if mostrar_experiencia else [],
        'cursos': perfil.cursos.all().order_by('-fecha_inicio') if mostrar_cursos else [],
        'reconocimientos': perfil.reconocimientos.all().order_by('-fecha') if mostrar_reconocimientos else [],
        'productos_academicos': perfil.productos_academicos.all().order_by('-fecha') if mostrar_productos_academicos else [],
        'productos_laborales': perfil.productos_laborales.all().order_by('-fecha') if mostrar_productos_laborales else [],
        'is_print': True,
        'mostrar_sidebar': mostrar_datos_personales,
    }
    
    return render(request, 'cv/print_preview.html', context)


def servir_foto(request, perfil_id):
    """Servir foto de perfil de forma protegida"""
    perfil = get_object_or_404(Perfil, id=perfil_id)
    
    if perfil.foto:
        return FileResponse(perfil.foto.open('rb'), content_type='image/jpeg')
    
    return HttpResponse(status=404)


def servir_certificado_experiencia(request, experiencia_id):
    """Servir certificado de experiencia"""
    from .models import ExperienciaLaboral
    
    experiencia = get_object_or_404(ExperienciaLaboral, id=experiencia_id)
    
    if not experiencia.certificado:
        return HttpResponse(status=404)
    
    # Determinar si es descarga o vista previa
    is_download = request.GET.get('download', '0') == '1'
    
    # Abrir el archivo
    file = experiencia.certificado.open('rb')
    
    # Determinar tipo de contenido
    filename = experiencia.certificado.name
    if filename.endswith('.pdf'):
        content_type = 'application/pdf'
    elif filename.endswith(('.jpg', '.jpeg')):
        content_type = 'image/jpeg'
    elif filename.endswith('.png'):
        content_type = 'image/png'
    else:
        content_type = 'application/octet-stream'
    
    response = FileResponse(file, content_type=content_type)
    
    if is_download:
        response['Content-Disposition'] = f'attachment; filename="certificado_{experiencia.id}.pdf"'
    else:
        response['Content-Disposition'] = f'inline; filename="certificado_{experiencia.id}.pdf"'
    
    return response


def servir_certificado_curso(request, curso_id):
    """Servir certificado de curso"""
    from .models import CursoRealizado
    
    curso = get_object_or_404(CursoRealizado, id=curso_id)
    
    if not curso.certificado:
        return HttpResponse(status=404)
    
    is_download = request.GET.get('download', '0') == '1'
    file = curso.certificado.open('rb')
    
    filename = curso.certificado.name
    if filename.endswith('.pdf'):
        content_type = 'application/pdf'
    elif filename.endswith(('.jpg', '.jpeg')):
        content_type = 'image/jpeg'
    elif filename.endswith('.png'):
        content_type = 'image/png'
    else:
        content_type = 'application/octet-stream'
    
    response = FileResponse(file, content_type=content_type)
    
    if is_download:
        response['Content-Disposition'] = f'attachment; filename="certificado_curso_{curso.id}.pdf"'
    else:
        response['Content-Disposition'] = f'inline; filename="certificado_curso_{curso.id}.pdf"'
    
    return response


def servir_certificado_reconocimiento(request, reconocimiento_id):
    """Servir certificado de reconocimiento"""
    from .models import Reconocimiento
    
    reconocimiento = get_object_or_404(Reconocimiento, id=reconocimiento_id)
    
    if not reconocimiento.certificado:
        return HttpResponse(status=404)
    
    is_download = request.GET.get('download', '0') == '1'
    file = reconocimiento.certificado.open('rb')
    
    filename = reconocimiento.certificado.name
    if filename.endswith('.pdf'):
        content_type = 'application/pdf'
    elif filename.endswith(('.jpg', '.jpeg')):
        content_type = 'image/jpeg'
    elif filename.endswith('.png'):
        content_type = 'image/png'
    else:
        content_type = 'application/octet-stream'
    
    response = FileResponse(file, content_type=content_type)
    
    if is_download:
        response['Content-Disposition'] = f'attachment; filename="certificado_reconocimiento_{reconocimiento.id}.pdf"'
    else:
        response['Content-Disposition'] = f'inline; filename="certificado_reconocimiento_{reconocimiento.id}.pdf"'
    
    return response

