"""funcionalidad del programa convertir romano a entero"""
romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, '':None}



def romano_a_entero(numero_romano):

    if numero_romano == "":#si no se ha introducido letra romana
        return "Error en formato"#error para cumplir condición de no puede estar vacío
    
    entero = 0
    numRepes = 1
    letraAnt = ""    
    
    
    for letra in numero_romano:#bucle para recorrer cada letra del número romano introducido
        
        if letra == letraAnt and numRepes == 3:#si la letra siguiente y la anterior son la misma y además se ha repetido 3 veces
            return "Error en formato"#error para cumplir condición de NO más de 3 repeticiones
        elif letra == letraAnt:#si la letra es igual a la anterior
            numRepes += 1 #me incrementas en uno el número de repeticiones
        else:#y si no son la misma letra y letraAnt
            numRepes = 1#colocas el número de repeticiones en 1

        if letra in romanos:#Si la letra introducida está en el diccionario me devuelves el valor entero
            entero += romanos[letra]#acumulo el valor de la letra romana
            
        else:#si no está en el diccionario
            return "Error en formato"#error para cumplir condición que debe ser letra romana I,V,X...
        
        letraAnt = letra#igualo letra nueva a letra anterior para saberla y así poder comparar si ya ha salido con anterioridad

    return entero