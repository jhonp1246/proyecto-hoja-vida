# 🚀 GUÍA PARA PUBLICAR EN RENDER.COM

## 📋 Prerequisitos

✅ Archivos ya preparados en el proyecto:
- `build.sh` - Script de construcción
- `runtime.txt` - Versión de Python
- `requirements.txt` - Dependencias actualizadas
- `settings.py` - Configurado para producción

---

## 🔧 PASO 1: Preparar el Proyecto Localmente

### 1.1 Inicializar Git (si no está inicializado)

```bash
git init
git add .
git commit -m "Preparar proyecto para Render"
```

### 1.2 Crear repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre del repo: `proyecto-hoja-vida` (o el que prefieras)
3. **NO** marques "Initialize with README"
4. Click "Create repository"

### 1.3 Subir el código a GitHub

```bash
git remote add origin https://github.com/TU_USUARIO/proyecto-hoja-vida.git
git branch -M main
git push -u origin main
```

---

## 🌐 PASO 2: Crear Cuenta en Render

1. Ve a https://render.com/
2. Click **"Get Started"** o **"Sign Up"**
3. Regístrate con GitHub (recomendado) o email
4. Verifica tu cuenta por email

---

## 🗄️ PASO 3: Crear Base de Datos PostgreSQL

1. En el Dashboard de Render, click **"New +"**
2. Selecciona **"PostgreSQL"**
3. Configuración:
   - **Name**: `hojadevida-db` (o el nombre que prefieras)
   - **Database**: `hojadevida`
   - **User**: (se genera automáticamente)
   - **Region**: Selecciona la más cercana (ej: Ohio, USA)
   - **Plan**: **Free** (suficiente para empezar)
4. Click **"Create Database"**
5. **IMPORTANTE**: Guarda la **Internal Database URL** que aparece
   - Ejemplo: `postgresql://user:pass@host/database`

---

## 🌍 PASO 4: Crear Web Service

1. En el Dashboard, click **"New +"**
2. Selecciona **"Web Service"**
3. Conecta tu repositorio de GitHub:
   - Click **"Connect a repository"**
   - Autoriza Render a acceder a GitHub
   - Selecciona tu repositorio `proyecto-hoja-vida`
4. Configuración del servicio:

   **Configuración Básica:**
   - **Name**: `mi-hoja-vida` (será tu URL: mi-hoja-vida.onrender.com)
   - **Region**: Misma que la base de datos
   - **Branch**: `main`
   - **Root Directory**: (dejar vacío)
   - **Runtime**: `Python 3`

   **Build & Deploy:**
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn project.wsgi:application`

5. **IMPORTANTE**: Antes de hacer deploy, configura las variables de entorno

---

## 🔐 PASO 5: Configurar Variables de Entorno

En la página de configuración del Web Service, ve a **"Environment"** y agrega:

```
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=genera-una-clave-segura-aqui-usa-50-caracteres-aleatorios
DATABASE_URL=postgresql://user:pass@host/database
ALLOWED_HOSTS=.onrender.com
```

**Para generar SECRET_KEY:**
```python
import secrets
print(secrets.token_urlsafe(50))
```

**Para DATABASE_URL:**
- Copia la "Internal Database URL" que guardaste en el Paso 3
- O ve a tu PostgreSQL database en Render → "Info" → Copia "Internal Database URL"

---

## 🚀 PASO 6: Hacer el Deploy

1. Una vez configuradas todas las variables, click **"Create Web Service"**
2. Render comenzará el despliegue automáticamente
3. Verás los logs en tiempo real:
   - Instalando dependencias...
   - Ejecutando build.sh...
   - Recolectando archivos estáticos...
   - Aplicando migraciones...
   - Iniciando servidor...

4. Espera a que aparezca: **"Your service is live"** (toma 5-10 minutos)

---

## ✅ PASO 7: Verificar el Deploy

1. Tu sitio estará en: `https://mi-hoja-vida.onrender.com`
2. Ve a: `https://mi-hoja-vida.onrender.com/admin/`
3. **IMPORTANTE**: Debes crear un superusuario

### Crear Superusuario en Render

**Opción 1: Desde Shell (Recomendado)**

1. En tu Web Service en Render, ve a **"Shell"** (menú lateral)
2. Click **"Connect"**
3. Ejecuta:
```bash
python manage.py createsuperuser
```
4. Completa usuario, email y contraseña

**Opción 2: Script desde Shell**

```bash
python manage.py shell
```

Luego:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@ejemplo.com', 'tu_password_segura')
exit()
```

---

## 📝 PASO 8: Configurar tu CV

1. Ingresa al admin: `https://tu-app.onrender.com/admin/`
2. Login con tu superusuario
3. Crea tu perfil con todos los datos
4. Agrega experiencias, cursos, etc.
5. Marca el perfil como "Activo"
6. Ve tu CV en: `https://tu-app.onrender.com/`

---

## 🔄 PASO 9: Actualizaciones Futuras

Cada vez que hagas cambios:

```bash
git add .
git commit -m "Descripción de los cambios"
git push origin main
```

Render detectará el push y **desplegará automáticamente** la nueva versión.

---

## ⚠️ IMPORTANTE: Archivos Estáticos y Media

### Limitaciones del Plan Free:

- Los archivos **estáticos** (CSS, JS) están cubiertos por WhiteNoise ✅
- Los archivos **media** (fotos, PDFs) se pierden al reiniciar el servidor ⚠️

### Solución para Archivos Media (Opcional):

Usar **Cloudinary** (gratis hasta 25GB):

1. Crea cuenta en https://cloudinary.com/
2. Instala: `pip install django-cloudinary-storage`
3. Agrega a `requirements.txt`
4. Configura en `settings.py`

---

## 🐛 Solución de Problemas Comunes

### Error: "Application failed to respond"
- Ve a Logs en Render
- Revisa que DATABASE_URL esté configurada
- Verifica que SECRET_KEY esté configurada

### Error: "Page not found (404)"
- Verifica ALLOWED_HOSTS en variables de entorno
- Asegúrate de que el dominio `.onrender.com` esté incluido

### Error: "Static files not loading"
- Verifica que `./build.sh` se ejecute correctamente
- Revisa logs: debe decir "X static files copied"

### Base de datos vacía
- Entra al Shell y ejecuta: `python manage.py migrate`
- Crea superusuario nuevamente

---

## 📊 Monitoreo

En el Dashboard de Render:

- **Logs**: Ver logs en tiempo real
- **Metrics**: CPU, Memoria, Requests
- **Events**: Historial de deploys
- **Shell**: Acceso a terminal del servidor

---

## 💰 Plan Free - Limitaciones

✅ **Incluye:**
- 750 horas/mes gratis
- PostgreSQL con 1GB
- Deploy automático desde GitHub
- SSL/HTTPS gratis
- Dominio .onrender.com

⚠️ **Limitaciones:**
- El servicio "duerme" tras 15 min de inactividad
- Primera carga puede tardar 30-50 segundos
- Archivos media no persisten

🎯 **Tip**: Para evitar que duerma, usa un servicio de ping (ej: UptimeRobot)

---

## 🎉 ¡Listo!

Tu CV profesional está ahora en línea y accesible desde cualquier lugar.

**URL Final:** `https://tu-nombre.onrender.com/`

Comparte esta URL en tu LinkedIn, GitHub, email, etc. 🚀

---

## 📞 Ayuda Adicional

- Documentación Render: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
- Comunidad Render: https://community.render.com/

**¡Éxito con tu Hoja de Vida en línea!** 🎊
