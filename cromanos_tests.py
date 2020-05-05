import unittest
import cromanos

class RomanNumberTest(unittest.TestCase):
    def test_symbols_romans(self):

        nr = cromanos.RomanNumber()

        self.assertEqual(nr.romano_a_entero('I'), 1)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(nr.romano_a_entero('V'), 5)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(nr.romano_a_entero('X'), 10)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(nr.romano_a_entero('L'), 50)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(nr.romano_a_entero('C'), 100)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(nr.romano_a_entero('D'), 500)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(nr.romano_a_entero('M'), 1000)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(nr.romano_a_entero('K'), 'Error en formato')#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(nr.romano_a_entero(''), 'Error en formato')#con assert nos aseguramos que NO se produzcan errores



if __name__ == "__main__":
    unittest.main()

