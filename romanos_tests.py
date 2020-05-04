"""Tests de pruebas para main.py números romanos"""


import unittest#para comprobar los errores
import romanos#para comprobar la funcionalidad del programa

class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romanos.romano_a_entero('I'), 1)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('V'), 5)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('X'), 10)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('L'), 50)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('C'), 100)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('D'), 500)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('M'), 1000)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('K'), 'Error en formato')#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero(''), 'Error en formato')#con assert nos aseguramos que NO se produzcan errores

    def test_repetitions(self):
        self.assertEqual(romanos.romano_a_entero('II'), 2)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('MMM'), 3000)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('KKK'), 'Error en formato')#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('MK'), 'Error en formato')#con assert nos aseguramos que NO se produzcan errores
    
    def test_only_three(self):
        self.assertEqual(romanos.romano_a_entero('IIII'), 'Error en formato')#con assert nos aseguramos que NO se produzcan errores

    def test_digitos_decrecientes(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'), 18)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('XI'), 11)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('XV'), 15)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('XX'), 20)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('CI'), 101)#con assert nos aseguramos que NO se produzcan errores
       
    
    def test_digitos_restan(self):
        self.assertEqual(romanos.romano_a_entero('XIX'), 19)#con assert nos aseguramos que NO se produzcan errores
       
    def test_resta_separacion_un_grado(self):
        self.assertEqual(romanos.romano_a_entero('XC'), 90)#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('XD'), "Error en formato")#con assert nos aseguramos que NO se produzcan errores  
        self.assertEqual(romanos.romano_a_entero('IL'), "Error en formato")#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('XM'), "Error en formato")#con assert nos aseguramos que NO se produzcan errores

    def test_resta_de_multiplos_5_NO(self):
        self.assertEqual(romanos.romano_a_entero('VC'), "Error en formato")#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('XCV'), 95)#con assert nos aseguramos que NO se produzcan errores

    def test_resta_un_solo_simbolo(self):
        self.assertEqual(romanos.romano_a_entero('XXL'), "Error en formato")#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('IXL'), "Error en formato")#con assert nos aseguramos que NO se produzcan errores
        self.assertEqual(romanos.romano_a_entero('XXX'), 30)#con assert nos aseguramos que NO se produzcan errores



if __name__ == "__main__":
    unittest.main()
