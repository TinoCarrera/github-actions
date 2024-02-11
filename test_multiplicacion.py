import unittest
from multiplicacion import multiplicar

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(multiplicar(5, 0), 0)

if __name__ == '__main__':
    unittest.main()
