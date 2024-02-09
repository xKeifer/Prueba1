import unittest
from func1 import *

class TestObtenerMayor(unittest.TestCase):
    def test_obtener_mayor(self):
        self.assertEqual(obtener_mayor(3, 7), 7)
        self.assertEqual(obtener_mayor(5, 2), 5)

if __name__ == '__main__':
    unittest.main()

