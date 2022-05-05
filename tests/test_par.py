# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import par_impar

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_par_impar(self):
        assert par_impar(0) == "par"
        assert par_impar(1) == "impar"
        assert par_impar(2) == "par"
        assert par_impar(3) == "impar"
        assert par_impar(4) == "par"
