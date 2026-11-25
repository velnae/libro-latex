import unittest
from presupuesto import evaluar_compra, soles


class PruebasPresupuesto(unittest.TestCase):
    def setUp(self):
        self.materiales = [("Cuadernos", 5, 450),
                          ("Lápices", 10, 120),
                          ("Cartulinas", 4, 300)]

    def test_normal(self):
        self.assertEqual(evaluar_compra(10000, self.materiales),
                         (4650, 5350, True))

    def test_exacto(self):
        self.assertEqual(evaluar_compra(4650, self.materiales),
                         (4650, 0, True))

    def test_insuficiente(self):
        self.assertEqual(evaluar_compra(4000, self.materiales),
                         (4650, -650, False))

    def test_vacio(self):
        self.assertEqual(evaluar_compra(0, []), (0, 0, True))

    def test_cantidad_invalida(self):
        with self.assertRaises(ValueError):
            evaluar_compra(1000, [("Lápiz", -1, 100)])

    def test_presupuesto_invalido(self):
        with self.assertRaises(ValueError):
            evaluar_compra(-1, [])

    def test_nombre_invalido(self):
        with self.assertRaises(ValueError):
            evaluar_compra(1000, [("", 1, 100)])

    def test_formato(self):
        self.assertEqual(soles(-650), "-S/ 6.50")

    def test_cantidad_cero(self):
        with self.assertRaises(ValueError):
            evaluar_compra(1000, [("Lápiz", 0, 100)])

    def test_precio_invalido(self):
        with self.assertRaises(ValueError):
            evaluar_compra(1000, [("Lápiz", 2, -1)])

    def test_precio_cero(self):
        self.assertEqual(evaluar_compra(0, [("Lápiz", 2, 0)]), (0, 0, True))
