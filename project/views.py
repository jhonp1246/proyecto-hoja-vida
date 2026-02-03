"""
Vistas auxiliares del proyecto
"""
from django.http import FileResponse, Http404
from django.conf import settings
import os


def serve_media(request, path):
    """
    Vista para servir archivos media en producción
    """
    try:
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        
        if not os.path.exists(file_path):
            raise Http404("Archivo no encontrado")
        
        # Determinar el tipo de contenido
        if path.endswith('.pdf'):
            content_type = 'application/pdf'
        elif path.endswith(('.jpg', '.jpeg')):
            content_type = 'image/jpeg'
        elif path.endswith('.png'):
            content_type = 'image/png'
        else:
            content_type = 'application/octet-stream'
        
        return FileResponse(open(file_path, 'rb'), content_type=content_type)
    except Exception as e:
        raise Http404(f"Error al servir archivo: {str(e)}")
