"""
Modelos para la aplicación CV
Incluye validaciones estrictas de fechas y ordenamiento cronológico
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date


def validar_fecha_no_futura(value):
    """Validar que la fecha no sea futura"""
    if value > date.today():
        raise ValidationError('La fecha no puede ser futura')


def validar_fecha_nacimiento(value):
    """Validar fecha de nacimiento razonable"""
    if value > date.today():
        raise ValidationError('La fecha de nacimiento no puede ser futura')
    if value.year < 1900:
        raise ValidationError('El año debe ser mayor a 1900')


def validar_fecha_minima_2000(value):
    """Validar que la fecha sea mayor a 2000"""
    if value > date.today():
        raise ValidationError('La fecha no puede ser futura')
    if value.year < 2000:
        raise ValidationError('El año debe ser mayor o igual a 2000')


def validar_telefono(value):
    """Validar que el teléfono contenga solo números, espacios, guiones y paréntesis"""
    import re
    if value and not re.match(r'^[\d\s\-\(\)\+]+$', value):
        raise ValidationError('El teléfono solo puede contener números, espacios, guiones, paréntesis y el símbolo +')


def validar_horas_positivas(value):
    """Validar que las horas sean mayores a 0"""
    if value is not None and value <= 0:
        raise ValidationError('Las horas deben ser mayores a 0')


class Perfil(models.Model):
    """Modelo para datos personales del perfil profesional"""
    
    SEXO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ]
    
    ESTADO_CIVIL_CHOICES = [
        ('Soltero', 'Soltero/a'),
        ('Casado', 'Casado/a'),
        ('Divorciado', 'Divorciado/a'),
        ('Viudo', 'Viudo/a'),
        ('Union Libre', 'Unión Libre'),
    ]
    
    # Datos básicos
    nombres = models.CharField('Nombres completos', max_length=200)
    identificacion = models.CharField('Cédula/Identificación', max_length=20, unique=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', validators=[validar_fecha_nacimiento])
    nacionalidad = models.CharField('Nacionalidad', max_length=100, default='Ecuatoriana')
    lugar_nacimiento = models.CharField('Lugar de nacimiento', max_length=200)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField('Estado civil', max_length=20, choices=ESTADO_CIVIL_CHOICES)
    
    # Contacto
    telefono_convencional = models.CharField('Teléfono convencional', max_length=15, blank=True, validators=[validar_telefono])
    telefono_fijo = models.CharField('Teléfono fijo', max_length=15, blank=True, validators=[validar_telefono])
    telefono_movil = models.CharField('Teléfono móvil', max_length=20, blank=True, validators=[validar_telefono])
    email = models.EmailField('Correo electrónico', blank=True)
    direccion = models.TextField('Dirección domiciliaria', blank=True)
    direccion_trabajo = models.CharField('Dirección de trabajo', max_length=200, blank=True)
    sitio_web = models.URLField('Sitio web personal', max_length=60, blank=True)
    
    # Otros
    licencia_conducir = models.BooleanField('Tiene licencia de conducir', default=False)
    tipo_licencia = models.CharField('Tipo de licencia', max_length=10, blank=True)
    sobre_mi = models.TextField('Sobre mí', help_text='Breve descripción profesional')
    foto = models.ImageField('Foto de perfil', upload_to='fotos/', blank=True, null=True)
    
    # Control de secciones visibles
    mostrar_experiencia = models.BooleanField('Mostrar experiencia laboral', default=True)
    mostrar_cursos = models.BooleanField('Mostrar cursos realizados', default=True)
    mostrar_reconocimientos = models.BooleanField('Mostrar reconocimientos', default=True)
    mostrar_productos_academicos = models.BooleanField('Mostrar productos académicos', default=True)
    mostrar_productos_laborales = models.BooleanField('Mostrar productos laborales', default=True)
    mostrar_venta_garage = models.BooleanField('Mostrar venta garage', default=True)
    
    activo = models.BooleanField('Perfil activo', default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-activo', '-fecha_actualizacion']
    
    def __str__(self):
        return self.nombres
    
    def edad(self):
        """Calcular edad actual"""
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )


class ExperienciaLaboral(models.Model):
    """Modelo para experiencias laborales"""
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='experiencias')
    cargo = models.CharField('Cargo/Puesto', max_length=200)
    empresa = models.CharField('Empresa/Institución', max_length=200)
    lugar_empresa = models.CharField('Lugar de la empresa', max_length=50, blank=True)
    email_empresa = models.EmailField('Email de la empresa', max_length=100, blank=True)
    sitio_web_empresa = models.URLField('Sitio web de la empresa', max_length=100, blank=True)
    nombre_contacto_empresarial = models.CharField('Nombre de contacto empresarial', max_length=100, blank=True)
    telefono_contacto_empresarial = models.CharField('Teléfono de contacto empresarial', max_length=60, blank=True, validators=[validar_telefono])
    fecha_inicio = models.DateField('Fecha de inicio', validators=[validar_fecha_minima_2000])
    fecha_fin = models.DateField('Fecha de fin', validators=[validar_fecha_no_futura], blank=True, null=True)
    actualmente_trabajando = models.BooleanField('Actualmente trabajando aquí', default=False)
    descripcion = models.TextField('Descripción de funciones', blank=True)
    certificado = models.FileField('Certificado (PDF/Imagen)', upload_to='certificados/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencias Laborales'
        ordering = ['-fecha_inicio']
    
    def clean(self):
        """Validaciones personalizadas"""
        super().clean()
        
        # Validar que fecha_fin sea posterior a fecha_inicio
        if self.fecha_fin and self.fecha_inicio:
            if self.fecha_fin < self.fecha_inicio:
                raise ValidationError({
                    'fecha_fin': 'La fecha de fin debe ser posterior a la fecha de inicio'
                })
        
        # Si actualmente trabaja, no debe tener fecha fin
        if self.actualmente_trabajando and self.fecha_fin:
            raise ValidationError({
                'fecha_fin': 'No debe especificar fecha de fin si actualmente trabaja aquí'
            })
    
    def __str__(self):
        return f"{self.cargo} - {self.empresa}"


class CursoRealizado(models.Model):
    """Modelo para cursos y capacitaciones"""
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='cursos')
    nombre_curso = models.CharField('Nombre del curso', max_length=300)
    institucion = models.CharField('Institución patrocinadora', max_length=200)
    nombre_contacto_auspicia = models.CharField('Nombre de contacto que auspicia', max_length=100, blank=True)
    telefono_contacto_auspicia = models.CharField('Teléfono de contacto que auspicia', max_length=60, blank=True, validators=[validar_telefono])
    email_empresa_patrocinadora = models.EmailField('Email empresa patrocinadora', max_length=60, blank=True)
    fecha_inicio = models.DateField('Fecha de inicio', validators=[validar_fecha_minima_2000])
    fecha_fin = models.DateField('Fecha de finalización', validators=[validar_fecha_no_futura])
    duracion_horas = models.IntegerField('Duración (horas)', blank=True, null=True, validators=[validar_horas_positivas])
    descripcion = models.TextField('Descripción', blank=True)
    certificado = models.FileField('Certificado (PDF/Imagen)', upload_to='certificados/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Curso Realizado'
        verbose_name_plural = 'Cursos Realizados'
        ordering = ['-fecha_inicio']
    
    def clean(self):
        """Validaciones personalizadas"""
        super().clean()
        
        if self.fecha_fin < self.fecha_inicio:
            raise ValidationError({
                'fecha_fin': 'La fecha de fin debe ser posterior a la fecha de inicio'
            })
    
    def __str__(self):
        return self.nombre_curso


class Reconocimiento(models.Model):
    """Modelo para reconocimientos y premios"""
    
    TIPO_RECONOCIMIENTO_CHOICES = [
        ('Académico', 'Académico'),
        ('Público', 'Público'),
        ('Privado', 'Privado'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='reconocimientos')
    titulo = models.CharField('Título del reconocimiento', max_length=300)
    tipo_reconocimiento = models.CharField('Tipo de reconocimiento', max_length=20, choices=TIPO_RECONOCIMIENTO_CHOICES)
    institucion = models.CharField('Entidad patrocinadora', max_length=200)
    nombre_contacto_auspicia = models.CharField('Nombre de contacto que auspicia', max_length=100, blank=True)
    telefono_contacto_auspicia = models.CharField('Teléfono de contacto que auspicia', max_length=60, blank=True, validators=[validar_telefono])
    fecha = models.DateField('Fecha del reconocimiento', validators=[validar_fecha_no_futura])
    descripcion = models.TextField('Descripción', blank=True)
    certificado = models.FileField('Certificado (PDF/Imagen)', upload_to='certificados/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Reconocimiento'
        verbose_name_plural = 'Reconocimientos'
        ordering = ['-fecha']
    
    def __str__(self):
        return self.titulo


class ProductoAcademico(models.Model):
    """Modelo para productos académicos (investigaciones, publicaciones, etc.)"""
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos_academicos')
    nombre = models.CharField('Nombre del producto', max_length=300)
    descripcion = models.TextField('Descripción')
    fecha = models.DateField('Fecha de publicación/creación', validators=[validar_fecha_no_futura])
    clasificador = models.CharField(
        'Clasificador (etiquetas separadas por comas)', 
        max_length=500,
        help_text='Ej: ingeniería,tecnologiasinformacion,basesdedatos,pregrado,docencia'
    )
    url = models.URLField('URL', blank=True)
    archivo = models.FileField('Archivo', upload_to='productos/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Producto Académico'
        verbose_name_plural = 'Productos Académicos'
        ordering = ['-fecha']
    
    def __str__(self):
        return self.nombre
    
    def get_etiquetas(self):
        """Obtener lista de etiquetas"""
        return [tag.strip() for tag in self.clasificador.split(',') if tag.strip()]


class ProductoLaboral(models.Model):
    """Modelo para productos laborales (proyectos, desarrollos, etc.)"""
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos_laborales')
    nombre = models.CharField('Nombre del producto', max_length=300)
    descripcion = models.TextField('Descripción')
    fecha = models.DateField('Fecha de creación/entrega', validators=[validar_fecha_no_futura])
    empresa = models.CharField('Empresa/Cliente', max_length=200, blank=True)
    tecnologias = models.CharField('Tecnologías utilizadas', max_length=500, blank=True)
    url = models.URLField('URL', blank=True)
    archivo = models.FileField('Archivo', upload_to='productos/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Producto Laboral'
        verbose_name_plural = 'Productos Laborales'
        ordering = ['-fecha']
    
    def __str__(self):
        return self.nombre


class VentaGarage(models.Model):
    """Modelo para artículos en venta"""
    
    ESTADO_CHOICES = [
        ('bueno', 'Bueno'),
        ('regular', 'Regular'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='ventas_garage')
    nombre = models.CharField('Nombre del producto', max_length=200)
    descripcion = models.TextField('Descripción')
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    estado = models.CharField('Estado', max_length=10, choices=ESTADO_CHOICES)
    fecha_publicacion = models.DateField('Fecha de publicación', validators=[validar_fecha_no_futura])
    imagen = models.ImageField('Imagen del producto', upload_to='garage/', blank=True, null=True)
    disponible = models.BooleanField('Disponible', default=True)
    
    class Meta:
        verbose_name = 'Artículo Venta Garage'
        verbose_name_plural = 'Venta Garage'
        ordering = ['-fecha_publicacion', '-disponible']
    
    def __str__(self):
        return self.nombre

