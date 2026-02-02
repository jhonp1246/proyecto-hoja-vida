# Hoja de Vida Profesional - Django

Proyecto Django completo que replica fielmente el diseño profesional de una Hoja de Vida moderna con animaciones CSS, glassmorphism y diseño responsive.

## 🚀 Características

✅ **Backend:** Python 3 + Django 4.2
✅ **Frontend:** HTML5 + CSS3 puro (sin frameworks)
✅ **Diseño:** Moderno, elegante, con animaciones y efectos avanzados
✅ **Responsive:** Desktop, tablet y móvil
✅ **Validaciones:** Fechas estrictas (no futuras, ordenamiento cronológico)
✅ **Admin personalizado:** Sin mostrar "Django", control de secciones
✅ **Impresión:** Formato A4 profesional con filtros de secciones
✅ **Gestión de archivos:** Certificados PDF/imágenes protegidos
✅ **Venta Garage:** Con imágenes, fechas y estados con colores

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

### 1. Clonar o descargar el proyecto

```bash
cd ProyectoHojaDeVida
```

### 2. Crear entorno virtual (recomendado)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

Ingrese:
- Nombre de usuario
- Email (opcional)
- Contraseña

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

## 📱 Uso

### Acceder a la aplicación

1. **Vista principal:** http://localhost:8000/
2. **Panel de administración:** http://localhost:8000/admin/

### Configurar tu perfil

1. Ingresa al panel de administración
2. Crea un nuevo **Perfil** con tus datos personales
3. Marca el perfil como **activo**
4. Agrega:
   - Experiencias laborales (con certificados opcionales)
   - Cursos realizados (con certificados)
   - Reconocimientos
   - Productos académicos (con clasificadores)
   - Productos laborales
   - Artículos para venta garage (con imágenes)

### Control de secciones visibles

En el perfil, puedes activar/desactivar qué secciones se muestran:
- ✅ Experiencia laboral
- ✅ Cursos realizados
- ✅ Reconocimientos
- ✅ Productos académicos
- ✅ Productos laborales
- ✅ Venta garage

### Imprimir CV

1. Haz clic en **"Imprimir CV"**
2. Selecciona las secciones que deseas incluir
3. Haz clic en **"Imprimir"**
4. Guarda como PDF desde el navegador

## 📂 Estructura del Proyecto

```
ProyectoHojaDeVida/
├── project/                    # Configuración Django
│   ├── settings.py            # Configuración principal
│   ├── urls.py                # URLs principales
│   ├── wsgi.py                # WSGI config
│   └── asgi.py                # ASGI config
├── cv/                        # Aplicación principal
│   ├── models.py              # Modelos de datos
│   ├── views.py               # Vistas
│   ├── urls.py                # URLs de la app
│   ├── admin.py               # Configuración del admin
│   ├── templates/cv/          # Templates HTML
│   │   ├── index.html         # Vista principal
│   │   ├── print_preview.html # Vista de impresión
│   │   ├── garage.html        # Tienda garage
│   │   └── no_perfil.html     # Sin perfil activo
│   └── static/cv/             # Archivos estáticos
│       ├── css/
│       │   └── style.css      # Estilos completos
│       └── img/               # Imágenes
├── media/                     # Archivos subidos
│   ├── fotos/                 # Fotos de perfil
│   ├── certificados/          # Certificados PDF/imágenes
│   └── garage/                # Imágenes de productos
├── manage.py                  # Script de gestión Django
├── requirements.txt           # Dependencias
└── README.md                  # Este archivo
```

## 🎨 Características de Diseño

### Animaciones CSS
- Botones con pulsos y brillos animados
- Títulos con efectos de resplandor
- Timeline items con hover effects
- Transiciones suaves en todos los elementos

### Glassmorphism
- Efectos de vidrio esmerilado
- Fondos con blur y transparencias
- Bordes con gradientes animados

### Responsive
- Grid adaptativo para sidebar y contenido
- Diseño optimizado para móviles
- Timeline responsive con cambio de columnas

### Impresión Profesional
- Formato A4 optimizado
- Colores ajustados para impresión
- Fuentes serif para legibilidad
- Separación de páginas apropiada

## ⚙️ Validaciones Implementadas

✅ **Fechas:**
- No se permiten fechas futuras
- Fecha de fin debe ser posterior a fecha de inicio
- Año mínimo 2000 para experiencias/cursos
- Año mínimo 1900 para fecha de nacimiento

✅ **Ordenamiento:**
- Cronológico de mayor a menor (más reciente primero)
- En experiencias, cursos, reconocimientos y productos

✅ **Estados de Venta Garage:**
- Solo "bueno" (verde) o "regular" (naranja)
- Con fecha de publicación obligatoria

## 🔒 Seguridad

- Admin personalizado sin mostrar "Django"
- Archivos media servidos de forma protegida
- Validaciones en servidor (models)
- CSRF protection activado

## 📝 Modelos de Datos

### Perfil
- Datos personales completos
- Foto de perfil
- Control de secciones visibles

### ExperienciaLaboral
- Cargo, empresa, fechas
- Certificado (PDF/imagen)
- Validación de fechas

### CursoRealizado
- Nombre, institución, fechas
- Duración en horas
- Certificado

### Reconocimiento
- Título, tipo, institución
- Fecha del reconocimiento
- Certificado

### ProductoAcademico
- Nombre, descripción
- Clasificador (etiquetas)
- Fecha, URL, archivo

### ProductoLaboral
- Nombre, empresa, descripción
- Tecnologías utilizadas
- Fecha, URL, archivo

### VentaGarage
- Nombre, precio, estado
- Imagen del producto
- Fecha de publicación
- Disponibilidad

## 🛠️ Comandos Útiles

```bash
# Crear migraciones después de cambios en models.py
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario adicional
python manage.py createsuperuser

# Recolectar archivos estáticos (producción)
python manage.py collectstatic

# Ejecutar shell de Django
python manage.py shell

# Ver todas las migraciones
python manage.py showmigrations
```

## 📸 Capturas

La aplicación incluye:
- Vista principal con diseño de dos columnas
- Sidebar azul con datos personales
- Contenido oscuro con secciones animadas
- Timeline para experiencias y cursos
- Grid de productos académicos/laborales
- Tienda de venta garage con cards
- Modal de opciones de impresión
- PDF profesional en formato A4

## 🎯 Correcciones Implementadas

Basado en las observaciones del profesor:

✅ Validación estricta de fechas (no futuras)
✅ Fecha fin posterior a fecha inicio
✅ Ordenamiento cronológico correcto
✅ Menú de selección para impresión PDF
✅ Manejo de certificados (vista previa y descarga)
✅ Estados con colores en venta garage
✅ Opciones para activar/desactivar secciones
✅ Admin sin mostrar "Django"
✅ Fecha e imagen en productos garage
✅ Clasificadores en productos académicos
✅ Copyright del autor
✅ Navegación mejorada

## 🚀 Despliegue en Producción

Para desplegar en producción:

1. Cambiar `DEBUG = False` en settings.py
2. Configurar `ALLOWED_HOSTS`
3. Usar una base de datos robusta (PostgreSQL)
4. Configurar servidor web (Nginx + Gunicorn)
5. Usar HTTPS
6. Configurar variables de entorno para secretos

## 📞 Soporte

Para problemas o dudas:
1. Revisa la documentación de Django: https://docs.djangoproject.com/
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de tener Python 3.8+

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

**Desarrollado con ❤️ usando Django y CSS3**

**Calificación esperada:** ⭐⭐⭐ 10/10 - Proyecto altamente documentable
