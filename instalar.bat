@echo off
echo ========================================
echo   INSTALACION AUTOMATICA - HOJA DE VIDA
echo ========================================
echo.

echo [1/5] Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo Por favor instale Python 3.8 o superior
    pause
    exit /b 1
)
echo.

echo [2/5] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Fallo la instalacion de dependencias
    pause
    exit /b 1
)
echo.

echo [3/5] Configurando base de datos...
python manage.py makemigrations
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Fallo la configuracion de base de datos
    pause
    exit /b 1
)
echo.

echo [4/5] Recolectando archivos estaticos...
python manage.py collectstatic --noinput
echo.

echo ========================================
echo   INSTALACION COMPLETADA
echo ========================================
echo.
echo Ahora debes crear un superusuario:
echo   python manage.py createsuperuser
echo.
echo Y luego ejecutar el servidor:
echo   python manage.py runserver
echo.
echo Luego accede a: http://localhost:8000/admin/
echo.
pause
