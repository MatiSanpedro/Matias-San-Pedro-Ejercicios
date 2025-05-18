#MIS FUNCIONES 

#FUNCION CALCULADORA

def suma (numero:float,numero2:float)-> float:
    operacion = numero + numero2
    return operacion

def resta (numero:float,numero2:float)-> float:
    operacion = numero - numero2
    return operacion    

def division(numero:float,numero2:float)-> float:
    operacion = numero / numero2 
    return operacion

def multiplicacion(numero:float,numero2:float)-> float:
    operacion = numero * numero2
    return operacion

def potencia(numero:float,numero2:float)->float:
    operacion = numero ** numero2 
    return operacion



#MOSTRAR DATOS 
def mostrar_datos(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(len(lista_a)):

        if len(lista_a[i]) < 8:
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}")
        else:
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}")    


#COPIAR LISTA
def copiar_lista(lista_a:list, lista_b:list)->list:
    nombres_originales = [-1] * len(lista_a)
    edades_originales = [-1] * len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i] = lista_a[i]
        edades_originales[i] = lista_b[i]
    
    return nombres_originales, edades_originales

#ORDENAR ASCENDENTE
def ordenar_ascendente(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if lista_c[i] > lista_c[j]:
            
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] > lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

#ORDENAR DESCENDENTE
def ordenar_descendente(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if lista_c[i] < lista_c[j]:
            
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] < lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

#SORT PROPIO
def ordenar(lista_a:list, lista_b:list, lista_c:list, primer_modo = 1, segundo_modo= 1) -> None:

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if (lista_c[i] > lista_c[j] and primer_modo == 1) or (lista_c[i] < lista_c[j] and primer_modo == 2):
                #SWAP(intercambio)
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if (lista_a[i] > lista_a[j] and segundo_modo == 1) or (lista_a[i] < lista_a[j] and segundo_modo == 2):
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar


####################
#encontrar numeros 
def contiene_numeros(cadena:str):
    contador = 0
    tiene = False
    while contador < len(cadena):
        codigo = ord(cadena[contador])
        if 48 <= codigo <= 57:
            tiene = True
        contador += 1
        
        
    return tiene


#LOWER
def lower_propio(cadena:str)-> str:
    
    palabra_minusculas = ""
    caracter=""
    for i in range(len(cadena)):
        if ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90: #si el numero encontrado en la lista esta entre 65 y 90
            caracter = chr(ord(cadena[i]) + 32) #Le sumo 32 y convierto en minuscula
        elif ord(cadena[i]) == 209: #Esto es para la letra Ñ 
            caracter = chr(ord(cadena[i])+32 ) #209 - 32 = 241(ñ)
        else:
            caracter = cadena[i]
        palabra_minusculas += caracter

    return palabra_minusculas


#UPPER PROPIO



#CONVERTIR STRING A NUMEROS ASCII
def convertir_cadena_a_numeros_ascii(cadena:str)->list:
    guardado = []
    for i in cadena:
        cadena = ord(i)
        guardado = guardado + [ord(i)]
    

    return  guardado

#convertir una lista de codigos a texto 
def recibe_numeros_retorna_lista_de_caracteres(cadena:int)->list:
    guardada = []
    #cadena = [67, 97, 115, 97]
    for i in cadena:
        cadena = chr(i)
        guardada = guardada + [chr(i)]
    return guardada

# UPPER PROPIO

def upper_propio(cadena:str)-> str:
    palabra_mayusculas = ""
    caracter=""
    for i in range(len(cadena)):
        if ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122: #si el numero encontrado en la lista esta entre 97 y 122
            caracter = chr(ord(cadena[i]) - 32) #Le sumo 32 y convierto en minuscula
        elif ord(cadena[i]) == 241: #Esto es para la letra Ñ 
            caracter = chr(ord(cadena[i])- 32 ) #241 - 32 = 209(ñ)
        else:
            caracter = cadena[i]
        palabra_mayusculas += caracter

    return palabra_mayusculas


def validar_datos_nombre(nombre:str): #devuelve True si hay letras,  False si hay otra cosa 
    verificado = ""
    bandera = True
    for i in range(len(nombre)):
            #valido si lo que tengo son letras mayuscula/minuscula, ñ y espacio 
            if (ord(nombre[i]) >=97 and ord(nombre[i]) <=122) or (ord(nombre[i]) >=65 and ord(nombre[i]) <=90): #esto valida mayuscula y minuscula
                verificado = nombre
                bandera = True 
                continue #cada vez que encuentro un dato valido, lo ignoro 
            if (ord(nombre[i]) == 241 or ord(nombre[i]) == 209): #esto valida las ñ - Ñ 
                verificado = nombre
                bandera = True
                continue
            if ord(nombre[i]) == 32: #esto valida si hay un espacio
                verificado = nombre
                bandera = True
                continue
            else:        #si tengo un dato que no encaja, imprime esto:
                
                bandera = False

    return bandera


def validar_datos_edad(edad:int): #verifica si lo ingresado son numeros
    bandera = True   #devuelve true o false
    numero = ""
    for i in range(len(edad)):
        numero = ord(edad[i])  #guardo el numero ascii en "numero"
        if numero <= 48 or numero >= 57 :  # si no esta dentro de los numeros (0-9) arroja False
            bandera = False
            continue
    return bandera 

