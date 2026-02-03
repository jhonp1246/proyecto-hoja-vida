# Configuración de Cloudinary para almacenamiento de archivos

## ¿Por qué Cloudinary?
Render.com tiene un sistema de archivos **efímero** - los archivos subidos se borran cada vez que se redesplega la aplicación. Cloudinary proporciona almacenamiento persistente y gratuito (hasta 25GB).

## Pasos para configurar Cloudinary

### 1. Crear cuenta en Cloudinary (GRATIS)
1. Ve a: https://cloudinary.com/users/register/free
2. Regístrate con tu email
3. Verifica tu correo

### 2. Obtener credenciales
1. Inicia sesión en Cloudinary
2. Ve al Dashboard
3. Copia estos 3 valores:
   - **Cloud Name**: cloudinary-xxxxx
   - **API Key**: 123456789012345
   - **API Secret**: aBcDeFgHiJkLmNoPqRsTuVwXyZ

### 3. Configurar variables de entorno en Render
1. Ve a tu aplicación en Render: https://dashboard.render.com
2. Click en tu servicio "mi-hoja-vida"
3. Ve a "Environment"
4. Agrega estas 3 variables:
   ```
   CLOUDINARY_CLOUD_NAME = tu-cloud-name
   CLOUDINARY_API_KEY = tu-api-key
   CLOUDINARY_API_SECRET = tu-api-secret
   ```
5. Click en "Save Changes"

### 4. Redesplegar
Render redesplegar automáticamente después de guardar las variables.

## ¿Qué hace esto?
- ✅ Los archivos subidos (fotos, certificados) se guardan en Cloudinary
- ✅ Los archivos persisten entre despliegues
- ✅ No se borran cuando Render reinicia
- ✅ URLs permanentes para todos los archivos

## Subir archivos existentes a Cloudinary
Después de configurar, deberás volver a subir tus archivos desde el panel de admin:
1. Ve a: https://mi-hoja-vida.onrender.com/admin/
2. Edita cada registro que tenga foto o certificado
3. Vuelve a subir el archivo
4. Guarda

Los nuevos archivos se guardarán automáticamente en Cloudinary.

## Alternativa (si no quieres usar Cloudinary)
Si prefieres no usar Cloudinary, puedes usar el almacenamiento local, pero tendrás que:
- Volver a subir los archivos cada vez que hagas un `git push`
- Los certificados desaparecerán con cada despliegue
