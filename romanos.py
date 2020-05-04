"""funcionalidad del programa convertir romano a entero"""
romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

existen = ["IX", "IV", "XL", "XC", "CD", "CM"]
 

def romano_a_entero(numero_romano):

    if numero_romano == "":#si no se ha introducido letra romana
        return "Error en formato"#error para cumplir condición de no puede estar vacío
    
    entero = 0#guardar el número entero final
    numRepes = 1#guardo número de repeticiones
    letraAnt = ""#guardo letra anterior para comprobar cumplir NO más de 3 repeticiones    
    fueResta = False
      
    
    for letra in numero_romano:#bucle para recorrer cada letra del número romano introducido

        if letra in romanos:
            if letraAnt == '' or romanos[letraAnt] >= romanos[letra]:
                entero += romanos[letra]
                fueResta = False
            else:
                if letraAnt + letra in existen and numRepes < 2 and not fueResta:#si letraAnta+letra está en lista existen y 
                    entero = entero - romanos[letraAnt] * 2 + romanos[letra]#número entero menos 2 veces el valor de letra anterior más valor nueva letra
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