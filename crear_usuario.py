import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if User.objects.filter(username='admin').exists():
    print('✓ Usuario admin ya existe')
else:
    User.objects.create_superuser('admin', 'admin@ejemplo.com', 'admin123')
    print('✓ Usuario admin creado exitosamente')
    print('  Usuario: admin')
    print('  Contraseña: admin123')
