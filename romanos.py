"""funcionalidad del programa convertir romano a entero"""
romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, '':None}



def romano_a_entero(numero_romano):

    if numero_romano == "":#si no se ha introducido letra romana
        return "Error en formato"#error para cumplir condición de no puede estar vacío
    
    entero = 0#guardar el número entero final
    numRepes = 1#guardo número de repeticiones
    letraAnt = ""#guardo letra anterior para comprobar cumplir NO más de 3 repeticiones    
    newVal = 0#guardo nuevo valor de la letra actual para cumplir que menor resta
    antVal = 0#guardo antiguo valor de la letra anterior para cumplir que menor resta
    
    
    for letra in numero_romano:#bucle para recorrer cada letra del número romano introducido
        
        if letra == letraAnt and numRepes == 3:#si la letra siguiente y la anterior son la misma y además se ha repetido 3 veces
            return "Error en formato"#error para cumplir condición de NO más de 3 repeticiones
        elif letra == letraAnt:#si la letra es igual a la anterior
            numRepes += 1 #me incrementas en uno el número de repeticiones
        else:#y si no son la misma letra y letraAnt
            numRepes = 1#colocas el número de repeticiones en 1

        if letra in romanos:#Si la letra introducida está en el diccionario me devuelves el valor entero
            newVal = romanos[letra]#nuevo valor es igual a valor correspondiente de la letra en el diccionario
            if antVal == 0:#si el valor anterior es 0 (primera pasada del for) 
                entero += newVal#entero es igual al nuevo valor
                antVal = newVal#valor nuevo pasa a valor anterior para comparar
            
            elif antVal < newVal:#si valor anterior es menor que nuevo valor (IL por ejemplo = 49)
                newVal -= antVal#resto antiguo valor al nuevo
                entero = newVal#guardo nuevo valor en entero y así tengo el resultado de la resta
                
            else:#esto es que valor anterior es mayor que nuevo valor (LI por ejemplo = 51)
                antVal = newVal#guardo nuevo valor en anterior para seguir comparando si hace falta
                entero += newVal#acumulo nuevo valor más lo que ya tenga entero
            
        
            
        else:#si no está en el diccionario
            return "Error en formato"#error para cumplir condición que debe ser letra romana I,V,X...
        
        letraAnt = letra#igualo letra nueva a letra anterior para saberla y así poder comparar si ya ha salido con anterioridad

    return entero