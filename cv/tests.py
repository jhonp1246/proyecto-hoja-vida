"""
Tests para la aplicación CV
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from .models import Perfil, ExperienciaLaboral, CursoRealizado


class PerfilModelTest(TestCase):
    """Tests para el modelo Perfil"""
    
    def setUp(self):
        self.perfil = Perfil.objects.create(
            nombres="Juan Pérez",
            identificacion="0912345678",
            fecha_nacimiento=date(1995, 3, 15),
            nacionalidad="Ecuatoriana",
            lugar_nacimiento="Quito",
            sexo="H",
            estado_civil="Soltero",
            sobre_mi="Profesional en TI"
        )
    
    def test_creacion_perfil(self):
        """Test crear perfil correctamente"""
        self.assertEqual(self.perfil.nombres, "Juan Pérez")
        self.assertTrue(self.perfil.activo)
    
    def test_calcular_edad(self):
        """Test calcular edad correctamente"""
        edad = self.perfil.edad()
        self.assertGreater(edad, 0)


class ValidacionFechasTest(TestCase):
    """Tests para validaciones de fechas"""
    
    def setUp(self):
        self.perfil = Perfil.objects.create(
            nombres="Test User",
            identificacion="0912345679",
            fecha_nacimiento=date(1990, 1, 1),
            nacionalidad="Ecuatoriana",
            lugar_nacimiento="Guayaquil",
            sexo="H",
            estado_civil="Soltero",
            sobre_mi="Test"
        )
    
    def test_fecha_futura_rechazada(self):
        """Test que rechaza fechas futuras"""
        fecha_futura = date.today() + timedelta(days=30)
        
        with self.assertRaises(ValidationError):
            exp = ExperienciaLaboral(
                perfil=self.perfil,
                cargo="Test",
                empresa="Test Corp",
                fecha_inicio=fecha_futura
            )
            exp.full_clean()
    
    def test_fecha_fin_anterior_rechazada(self):
        """Test que rechaza fecha fin anterior a fecha inicio"""
        exp = ExperienciaLaboral(
            perfil=self.perfil,
            cargo="Test",
            empresa="Test Corp",
            fecha_inicio=date(2023, 6, 1),
            fecha_fin=date(2023, 1, 1)
        )
        
        with self.assertRaises(ValidationError):
            exp.clean()
