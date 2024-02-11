import unittest
from division import dividir

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(3, 2), 1.5)
        self.assertEqual(dividir(10, 5), 2.0)
        self.assertEqual(dividir(5, 0), "No se puede dividir entre cero")

if __name__ == '__main__':
    unittest.main()
