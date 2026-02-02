# 🎬 GUÍA DE DEMOSTRACIÓN DEL PROYECTO

## Preparación previa (10 minutos antes)

### 1. Verificar instalación
```bash
python --version  # Debe ser 3.8+
pip list | findstr Django  # Verificar Django instalado
```

### 2. Iniciar servidor
```bash
python manage.py runserver
```

### 3. Abrir navegador
- Tab 1: http://localhost:8000/
- Tab 2: http://localhost:8000/admin/

---

## 🎯 SCRIPT DE DEMOSTRACIÓN (15 minutos)

### PARTE 1: Presentación del Diseño (3 min)

**Mostrar página principal:**
1. "Este es el diseño replicado fielmente de la página original"
2. Señalar características visuales:
   - ✨ Sidebar azul con gradiente
   - ✨ Contenido oscuro con glassmorphism
   - ✨ Animaciones en botones (hover)
   - ✨ Timeline con efectos

3. Hacer hover en elementos:
   - Botones superiores (pulsos y brillos)
   - Items de timeline (desplazamiento)
   - Tarjetas de productos (elevación)

4. Scroll suave para mostrar todas las secciones

### PARTE 2: Validaciones Estrictas (4 min)

**Ir al admin:**
1. Login con credenciales
2. Ir a "Experiencias Laborales" → "Agregar"

**Demostrar validaciones:**

**Prueba 1: Fecha futura**
```
Cargo: Test
Empresa: Test Corp
Fecha inicio: [fecha de mañana]
→ Click Guardar
```
**Resultado:** ❌ Error: "La fecha no puede ser futura"

**Prueba 2: Fecha fin anterior**
```
Fecha inicio: 01/06/2023
Fecha fin: 01/01/2023
→ Click Guardar
```
**Resultado:** ❌ Error: "La fecha fin debe ser posterior a la fecha inicio"

**Prueba 3: Datos correctos**
```
Fecha inicio: 01/01/2022
Fecha fin: 31/12/2023
→ Click Guardar
```
**Resultado:** ✅ Guardado exitosamente

3. **Mostrar ordenamiento:**
   - Volver a lista de experiencias
   - Señalar: "Ordenadas de más reciente a más antigua automáticamente"

### PARTE 3: Control de Secciones (2 min)

**Ir a Perfiles → Editar perfil activo:**

1. Scroll hasta "Control de Secciones Visibles"
2. **Demostrar:**
   - Desmarcar "Mostrar experiencia laboral"
   - Guardar
   - Volver a la página principal
   - "La sección de experiencia desapareció"
   
3. **Volver a marcar:**
   - Volver al admin
   - Marcar nuevamente
   - Guardar
   - Refrescar página principal
   - "La sección volvió a aparecer"

### PARTE 4: Gestión de Certificados (2 min)

**Volver a una experiencia:**
1. Hacer clic en "Vista previa" de un certificado
   - "Se abre en nueva pestaña"
   - "Visor embebido para no descargar automáticamente"

2. Hacer clic en "Descargar PDF"
   - "Descarga directa del archivo"

### PARTE 5: Impresión Profesional (3 min)

**Click en "Imprimir CV":**

1. **Mostrar filtros:**
   - "Puedo seleccionar qué secciones incluir"
   - Desmarcar "Venta Garage"
   - "La vista previa se actualiza en tiempo real"

2. **Click en Imprimir:**
   - Abrir diálogo de impresión del navegador
   - "Guardar como PDF" (no imprimir realmente)
   - Mostrar: "Formato A4 profesional"
   - Señalar: "Colores optimizados para papel"

3. **Abrir el PDF generado:**
   - "Diseño limpio y profesional"
   - "Perfecto para enviar a empleadores"

### PARTE 6: Venta Garage (1 min)

**Click en "Ver Tienda":**
1. Mostrar productos con:
   - 📷 Imágenes
   - 📅 Fecha de publicación
   - 🏷️ Estados con colores (Bueno=verde, Regular=naranja)
   - 💰 Precios

---

## 🎨 PUNTOS CLAVE A ENFATIZAR

### Durante la demostración, mencionar:

1. **"Sin frameworks frontend"**
   - Todo el CSS es puro
   - Las animaciones son @keyframes nativos

2. **"Validaciones infalibles"**
   - Imposible guardar fechas futuras
   - Control automático de coherencia

3. **"Admin profesional"**
   - No se ve "Django" por ningún lado
   - Todo personalizado

4. **"Responsive completo"**
   - (Opcional: abrir DevTools y cambiar a móvil)
   - "Funciona en cualquier dispositivo"

5. **"Ordenamiento automático"**
   - "No hay que ordenar manualmente"
   - "Siempre muestra lo más reciente primero"

---

## 🚨 POSIBLES PREGUNTAS Y RESPUESTAS

**P: ¿Cómo evitas las fechas futuras?**
R: "Validadores personalizados en los modelos de Django que comparan con date.today()"

**P: ¿Por qué no se ve 'Django' en el admin?**
R: "Configuré admin.site.site_header y site_title en urls.py"

**P: ¿Cómo funciona el ordenamiento?**
R: "Meta.ordering = ['-fecha_inicio'] en cada modelo"

**P: ¿Es responsive?**
R: "Sí, uso CSS Grid y Media Queries para adaptarlo"

**P: ¿Qué pasa si no hay perfil activo?**
R: "Muestra una página especial indicando que debe crear un perfil"

**P: ¿Los certificados están protegidos?**
R: "Sí, se sirven a través de vistas Django, no directamente desde /media/"

---

## 📋 CHECKLIST PRE-DEMOSTRACIÓN

- [ ] Servidor corriendo (sin errores en consola)
- [ ] Al menos 1 perfil activo
- [ ] 2-3 experiencias laborales (con certificados)
- [ ] 1-2 cursos
- [ ] 1 reconocimiento
- [ ] Productos académicos y laborales
- [ ] 2-3 artículos en venta garage (con imágenes)
- [ ] Admin accesible (usuario/contraseña probados)
- [ ] Navegador con tabs abiertos

---

## 🎭 TIPS DE PRESENTACIÓN

1. **Habla con confianza:** "Este proyecto implementa TODAS las correcciones mencionadas"

2. **Sé específico:** No digas "tiene validaciones", di "rechaza fechas futuras con ValidationError"

3. **Muestra, no cuentes:** Demuestra cada característica en vivo

4. **Anticipa problemas:** Ten datos de prueba preparados

5. **Enfatiza lo único:** "Única hoja de vida con estos efectos CSS sin usar frameworks"

---

## ⏱️ TIMING SUGERIDO

- 0:00-3:00 → Diseño visual
- 3:00-7:00 → Validaciones en vivo
- 7:00-9:00 → Control de secciones
- 9:00-11:00 → Certificados
- 11:00-14:00 → Impresión con filtros
- 14:00-15:00 → Venta Garage + Cierre

---

## 🎯 CIERRE IMPACTANTE

**Frase final sugerida:**

"Este proyecto no solo replica el diseño original, sino que lo mejora con validaciones robustas, control granular de contenido, y un sistema de impresión profesional. Cada una de las observaciones del profesor fue implementada, resultando en una aplicación Django lista para producción."

**Mostrar documentación:**
- "Incluye README completo"
- "Guía rápida de instalación"
- "Scripts automáticos para Windows"
- "Tests unitarios"
- "Documento de correcciones implementadas"

---

## 🌟 EXTRAS (si hay tiempo)

- Mostrar el código fuente brevemente (models.py, admin.py)
- Abrir DevTools y mostrar responsive
- Ejecutar tests: `python manage.py test cv`
- Mostrar .gitignore y estructura de carpetas

---

**¡Éxito en tu demostración!** 🚀

Recuerda: Este proyecto está **completamente terminado** y **listo para impresionar**.
