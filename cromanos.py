"""Ejercicio romano convertido a clase"""

class RomanNumber():
    __symbols = {'M':1000, 
    'CM':900, 
    'D':500, 
    'CD':400, 
    'C':100, 
    'XC':90, 
    'L':50, 
    'XL':40, 
    'X':10, 
    'IX':9, 
    'V':5, 
    'IV':4, 
    'I':1}

    def romano_a_entero(self, numero_romano):

        if numero_romano == "":#si no se ha introducido letra romana
            return "Error en formato"#error para cumplir condición de no puede estar vacío
        
        entero = 0#guardar el número entero final
        numRepes = 1#guardo número de repeticiones
        letraAnt = ""#guardo letra anterior para comprobar cumplir NO más de 3 repeticiones    
        fueResta = False#para comprobar si ha sido resta
        
        
        for letra in numero_romano:#bucle para recorrer cada letra del número romano introducido

            if letra in self.__symbols:
                if letraAnt == '' or self.__symbols[letraAnt] >= self.__symbols[letra]:#si letra está vacía o el valor de letra anterior es mayor o igual a valor letra actual
                    entero += self.__symbols[letra]#sumatorio de entero más entero y valor letra actual
                    fueResta = False
                else:
                    if letraAnt + letra in self.__symbols.keys() and numRepes < 2 and not fueResta:#si letraAnta+letra está en diccionario buscado por clave y número de repeticiones es menor de 2 y no ha sido resta
                        entero = entero - self.__symbols[letraAnt] * 2 + self.__symbols[letra]#número entero menos 2 veces el valor de letra anterior más valor nueva letra
                        fueResta = True
                    else:
                        return "Error en formato"
            else:#si no está en el diccionario
                return "Error en formato"#error para cumplir condición que debe ser letra romana I,V,X...

            if letra == letraAnt and numRepes == 3:#si la letra siguiente y la anterior son la misma y además se ha repetido 3 veces
                return "Error en formato"#error para cumplir condición de NO más de 3 repeticiones
            elif letra == letraAnt:#si la letra es igual a la anterior
                numRepes += 1 #me incrementas en uno el número de repeticiones
            else:#y si no son la misma letra y letraAnt
                numRepes = 1#colocas el número de repeticiones en 1

            
            letraAnt = letra#igualo letra nueva a letra anterior para saberla y así poder comparar si ya ha salido con anterioridad

        return entero


    def entero_a_romano(self, valor):
        if valor > 3999:
            return "Overflow"
        
        componentes = self.__descomponer(valor)

        res = ""
        for valor in componentes:
            while valor > 0:
                k, v = self.__busca_valor_menor_o_igual(valor)
                valor -= v
                res += k
            
        return res

    def __busca_valor_menor_o_igual(self,v):
        for key, value in self.__symbols.items():
            if value <= v:
                return key, value

    def __descomponer(self, numero):
        res = []
        for orden in range(3,0,-1):
            resto = numero % 10**orden
            res.append(numero-resto)
            numero = resto
        res.append(numero)
        return res