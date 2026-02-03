"""
Configuración del panel de administración
Personalizado para ocultar 'Django' y mejorar UX
"""

from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.safestring import mark_safe
from .models import (
    Perfil, ExperienciaLaboral, CursoRealizado, 
    Reconocimiento, ProductoAcademico, ProductoLaboral, VentaGarage
)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    """Admin para el perfil profesional"""
    
    fieldsets = (
        ('Datos Personales', {
            'fields': ('nombres', 'identificacion', 'fecha_nacimiento', 'nacionalidad', 
                      'lugar_nacimiento', 'sexo', 'estado_civil', 'foto')
        }),
        ('Contacto', {
            'fields': ('telefono_convencional', 'telefono_fijo', 'telefono_movil', 'email', 
                      'direccion', 'direccion_trabajo', 'sitio_web')
        }),
        ('Información Adicional', {
            'fields': ('licencia_conducir', 'tipo_licencia', 'sobre_mi')
        }),
        ('Control de Secciones Visibles', {
            'fields': ('mostrar_experiencia', 'mostrar_cursos', 'mostrar_reconocimientos',
                      'mostrar_productos_academicos', 'mostrar_productos_laborales', 'mostrar_venta_garage'),
            'description': 'Seleccione las secciones que desea mostrar en el CV'
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )
    
    list_display = ('nombres', 'identificacion', 'email', 'telefono_movil', 'activo', 'edad_display')
    list_filter = ('activo', 'sexo', 'estado_civil')
    search_fields = ('nombres', 'identificacion', 'email')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    
    def edad_display(self, obj):
        return f"{obj.edad()} años"
    edad_display.short_description = 'Edad'


@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    """Admin para experiencias laborales"""
    
    list_display = ('cargo', 'empresa', 'fecha_inicio', 'fecha_fin', 'actualmente_trabajando', 'tiene_certificado')
    list_filter = ('actualmente_trabajando', 'fecha_inicio')
    search_fields = ('cargo', 'empresa', 'descripcion')
    date_hierarchy = 'fecha_inicio'
    
    fieldsets = (
        (None, {
            'fields': ('perfil', 'cargo', 'empresa', 'lugar_empresa')
        }),
        ('Contacto Empresarial', {
            'fields': ('email_empresa', 'sitio_web_empresa', 'nombre_contacto_empresarial', 
                      'telefono_contacto_empresarial')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin', 'actualmente_trabajando'),
            'description': 'IMPORTANTE: La fecha de fin debe ser posterior a la de inicio. No se permiten fechas futuras.'
        }),
        ('Detalles', {
            'fields': ('descripcion', 'certificado')
        }),
    )
    
    def tiene_certificado(self, obj):
        if obj.certificado:
            return mark_safe('<span style="color: green;">✓ Sí</span>')
        return mark_safe('<span style="color: red;">✗ No</span>')
    tiene_certificado.short_description = 'Certificado'


@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    """Admin para cursos realizados"""
    
    list_display = ('nombre_curso', 'institucion', 'fecha_inicio', 'fecha_fin', 'duracion_horas', 'tiene_certificado')
    list_filter = ('fecha_inicio', 'institucion')
    search_fields = ('nombre_curso', 'institucion', 'descripcion')
    date_hierarchy = 'fecha_inicio'
    
    fieldsets = (
        (None, {
            'fields': ('perfil', 'nombre_curso', 'institucion')
        }),
        ('Contacto Patrocinador', {
            'fields': ('nombre_contacto_auspicia', 'telefono_contacto_auspicia', 
                      'email_empresa_patrocinadora')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin', 'duracion_horas'),
            'description': 'IMPORTANTE: La fecha de fin debe ser posterior a la de inicio. No se permiten fechas futuras.'
        }),
        ('Detalles', {
            'fields': ('descripcion', 'certificado')
        }),
    )
    
    def tiene_certificado(self, obj):
        if obj.certificado:
            return mark_safe('<span style="color: green;">✓ Sí</span>')
        return mark_safe('<span style="color: red;">✗ No</span>')
    tiene_certificado.short_description = 'Certificado'


@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    """Admin para reconocimientos"""
    
    list_display = ('titulo', 'tipo_reconocimiento', 'institucion', 'fecha', 'tiene_certificado')
    list_filter = ('tipo_reconocimiento', 'fecha')
    search_fields = ('titulo', 'institucion', 'descripcion')
    date_hierarchy = 'fecha'
    
    fieldsets = (
        (None, {
            'fields': ('perfil', 'titulo', 'tipo_reconocimiento', 'institucion')
        }),
        ('Contacto Patrocinador', {
            'fields': ('nombre_contacto_auspicia', 'telefono_contacto_auspicia')
        }),
        ('Fecha', {
            'fields': ('fecha',),
            'description': 'IMPORTANTE: No se permiten fechas futuras.'
        }),
        ('Detalles', {
            'fields': ('descripcion', 'certificado')
        }),
    )
    
    def tiene_certificado(self, obj):
        if obj.certificado:
            return mark_safe('<span style="color: green;">✓ Sí</span>')
        return mark_safe('<span style="color: red;">✗ No</span>')
    tiene_certificado.short_description = 'Certificado'


@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    """Admin para productos académicos"""
    
    list_display = ('nombre', 'fecha', 'preview_clasificador')
    list_filter = ('fecha',)
    search_fields = ('nombre', 'descripcion', 'clasificador')
    date_hierarchy = 'fecha'
    
    fieldsets = (
        (None, {
            'fields': ('perfil', 'nombre')
        }),
        ('Fecha', {
            'fields': ('fecha',),
            'description': 'IMPORTANTE: No se permiten fechas futuras.'
        }),
        ('Detalles', {
            'fields': ('descripcion', 'clasificador', 'url', 'archivo')
        }),
    )
    
    def preview_clasificador(self, obj):
        tags = obj.get_etiquetas()[:3]
        return ', '.join(tags) + ('...' if len(obj.get_etiquetas()) > 3 else '')
    preview_clasificador.short_description = 'Clasificador'


@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    """Admin para productos laborales"""
    
    list_display = ('nombre', 'empresa', 'fecha', 'preview_tecnologias')
    list_filter = ('fecha',)
    search_fields = ('nombre', 'descripcion', 'tecnologias', 'empresa')
    date_hierarchy = 'fecha'
    
    fieldsets = (
        (None, {
            'fields': ('perfil', 'nombre', 'empresa')
        }),
        ('Fecha', {
            'fields': ('fecha',),
            'description': 'IMPORTANTE: No se permiten fechas futuras.'
        }),
        ('Detalles', {
            'fields': ('descripcion', 'tecnologias', 'url', 'archivo')
        }),
    )
    
    def preview_tecnologias(self, obj):
        if obj.tecnologias:
            return obj.tecnologias[:50] + ('...' if len(obj.tecnologias) > 50 else '')
        return '-'
    preview_tecnologias.short_description = 'Tecnologías'


@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'estado_display', 'fecha_publicacion', 'disponible', 'preview_imagen')
    list_filter = ('disponible', 'estado', 'fecha_publicacion')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion', '-disponible')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('perfil', 'nombre', 'precio')
        }),
        ('Detalles', {
            'fields': ('descripcion', 'estado', 'imagen')
        }),
        ('Publicación', {
            'fields': ('fecha_publicacion', 'disponible'),
            'description': 'IMPORTANTE: No se permiten fechas futuras.'
        }),
    )
    
    def estado_display(self, obj):
        colores = {
            'bueno': '#28a745',
            'regular': '#ff9800'
        }
        color = colores.get(obj.estado, '#6c757d')
        return mark_safe(f'<span style="color: {color}; font-weight: bold;">●</span> {obj.get_estado_display()}')
    estado_display.short_description = 'Estado'
    
    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.imagen.url
            )
        return '-'
    preview_imagen.short_description = 'Vista previa'
