# 🎯 RESUMEN RÁPIDO - Deploy en Render

## ✅ Archivos ya configurados

- ✅ `build.sh` - Script de construcción
- ✅ `runtime.txt` - Python 3.11
- ✅ `requirements.txt` - Con gunicorn, whitenoise, psycopg2
- ✅ `settings.py` - Configurado para producción
- ✅ `.gitignore` - Archivos a ignorar

## 🚀 Comandos Rápidos

### 1. Subir a GitHub

```bash
git init
git add .
git commit -m "Proyecto Hoja de Vida listo para deploy"
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git branch -M main
git push -u origin main
```

### 2. En Render.com

**PostgreSQL Database:**
- Name: `hojadevida-db`
- Region: Ohio (US East)
- Plan: Free

**Web Service:**
- Build Command: `./build.sh`
- Start Command: `gunicorn project.wsgi:application`

**Variables de entorno:**
```
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=[genera una clave de 50 caracteres]
DATABASE_URL=[copia de la base de datos PostgreSQL]
ALLOWED_HOSTS=.onrender.com
```

### 3. Crear superusuario (en Shell de Render)

```bash
python manage.py createsuperuser
```

## 📖 Documentación Completa

Lee `DEPLOY_RENDER.md` para instrucciones detalladas paso a paso.

## 🔗 URLs Importantes

- Tu sitio: `https://TU-APP.onrender.com/`
- Admin: `https://TU-APP.onrender.com/admin/`
- Render Dashboard: https://dashboard.render.com/

## ⏱️ Tiempo estimado

- Configuración inicial: 15-20 minutos
- Primer deploy: 5-10 minutos
- Deploys posteriores: 3-5 minutos (automáticos)

---

**¿Problemas?** Consulta la sección "Solución de Problemas" en `DEPLOY_RENDER.md`
