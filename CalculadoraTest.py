from unittest import TestCase

autor = "oscar"

import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")
