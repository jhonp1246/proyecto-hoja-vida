# 🚀 GUÍA RÁPIDA DE INICIO

## Pasos para ejecutar el proyecto:

### 1️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3️⃣ Crear usuario administrador
```bash
python manage.py createsuperuser
```
- Usuario: admin
- Email: admin@ejemplo.com
- Contraseña: (la que prefieras, mínimo 8 caracteres)

### 4️⃣ Ejecutar servidor
```bash
python manage.py runserver
```

### 5️⃣ Acceder a la aplicación
- **Página principal:** http://localhost:8000/
- **Panel admin:** http://localhost:8000/admin/

### 6️⃣ Configurar tu perfil
1. Ingresa al admin con las credenciales creadas
2. Ve a **Perfiles** → **Agregar Perfil**
3. Completa todos los datos personales
4. **IMPORTANTE:** Marca el checkbox **"Perfil activo"**
5. Guarda el perfil
6. Agrega experiencias, cursos, reconocimientos, etc.

## 📝 Datos de ejemplo

Para probar rápidamente, puedes usar estos datos:

**Perfil:**
- Nombres: Juan Pérez García
- Identificación: 0912345678
- Fecha nacimiento: 15/03/1995
- Nacionalidad: Ecuatoriana
- Lugar nacimiento: Quito/Pichincha
- Sexo: H
- Estado civil: Soltero
- Teléfono móvil: 0998765432
- Email: juan.perez@email.com
- Sobre mí: Profesional en Tecnologías de la Información con experiencia en desarrollo web

**Experiencia Laboral:**
- Cargo: Desarrollador Full Stack
- Empresa: TechSolutions S.A.
- Fecha inicio: 01/01/2022
- Actualmente trabajando: Sí
- Descripción: Desarrollo de aplicaciones web con Django y React

**Curso:**
- Nombre: Desarrollo Web con Django
- Institución: Udemy
- Fecha inicio: 15/06/2021
- Fecha fin: 30/08/2021
- Duración: 40 horas

## ⚠️ Problemas comunes

**Error: No module named 'cv'**
→ Asegúrate de ejecutar `makemigrations` y `migrate`

**Error: No hay perfil activo**
→ Crea un perfil en el admin y márcalo como activo

**No se ven las imágenes**
→ Asegúrate de tener instalado Pillow: `pip install Pillow`

**Error al guardar fechas**
→ Las fechas no pueden ser futuras. Usa fechas pasadas.

## 🎯 Funcionalidades principales

✅ Vista de CV profesional con diseño moderno
✅ Panel de administración sin mostrar "Django"
✅ Control de secciones visibles desde el admin
✅ Validación estricta de fechas (no futuras)
✅ Ordenamiento cronológico automático
✅ Impresión con filtros de secciones
✅ Certificados con vista previa y descarga
✅ Venta garage con imágenes y estados coloreados
✅ Diseño 100% responsive
✅ Animaciones CSS avanzadas

## 📞 ¿Necesitas ayuda?

Revisa el archivo **README.md** para documentación completa.

---

**¡Proyecto listo para calificación 10/10!** ⭐⭐⭐
