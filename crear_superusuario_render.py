"""
Script para crear superusuario automáticamente en el primer deploy
Ejecutar: python crear_superusuario_render.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Configuración del superusuario
username = 'admin'
email = 'admin@ejemplo.com'
password = 'admin123'  # CÁMBIALA después de crear

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'✅ Superusuario "{username}" creado exitosamente')
    print(f'   Email: {email}')
    print(f'   Password: {password}')
    print('   ⚠️  CAMBIA LA CONTRASEÑA INMEDIATAMENTE DESDE EL ADMIN')
else:
    print(f'❌ El usuario "{username}" ya existe')
