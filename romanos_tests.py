"""Tests de pruebas para main.py números romanos"""


import unittest#para comprobar los errores
import romanos#para comprobar la funcionalidad del programa

class RomanToIntegerTest(unittest.TestCase):

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

class IntegerToRomanTest(unittest.TestCase):
    def test_traduccion_grupos_de_valor_simples(self):
        self.assertEqual(romanos.entero_a_romano(1), "I")
        self.assertEqual(romanos.entero_a_romano(10), "X")
        self.assertEqual(romanos.entero_a_romano(5), "V")
        self.assertEqual(romanos.entero_a_romano(50), "L")
        self.assertEqual(romanos.entero_a_romano(100), "C")
        self.assertEqual(romanos.entero_a_romano(500), "D")
        self.assertEqual(romanos.entero_a_romano(1000), "M")

    def test_traduccion_grupos_de_valor_complejos_unidades(self):
        self.assertEqual(romanos.entero_a_romano(2), "II")
        self.assertEqual(romanos.entero_a_romano(3), "III")
        self.assertEqual(romanos.entero_a_romano(4), "IV")
        self.assertEqual(romanos.entero_a_romano(6), "VI")
        self.assertEqual(romanos.entero_a_romano(7), "VII")
        self.assertEqual(romanos.entero_a_romano(8), "VIII")
        self.assertEqual(romanos.entero_a_romano(9), "IX")
        self.assertEqual(romanos.entero_a_romano(30), "XXX")
        self.assertEqual(romanos.entero_a_romano(400), "CD")
        self.assertEqual(romanos.entero_a_romano(3000), "MMM")
        
    def test_busca_valor(self):
        self.assertEqual(romanos.busca_valor_menor_o_igual(2), ("I", 1))
        self.assertEqual(romanos.busca_valor_menor_o_igual(5), ("V", 5))
        self.assertEqual(romanos.busca_valor_menor_o_igual(7), ("V", 5))

    def test_descomponer(self):
        self.assertEqual(romanos.descomponer(1492), [1000,400,90,2])
        self.assertEqual(romanos.descomponer(2342), [2000,300,40,2])

    def test_entero_a_romano(self):
        self.assertEqual(romanos.entero_a_romano(1492), "MCDXCII")
        self.assertEqual(romanos.entero_a_romano(3999), "MMMCMXCIX")
        self.assertEqual(romanos.entero_a_romano(4000), "Overflow")




if __name__ == "__main__":
    unittest.main()
