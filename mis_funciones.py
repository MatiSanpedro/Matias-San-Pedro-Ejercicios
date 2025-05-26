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


def maximo_numeros (numero_1:int,numero_2:int,numero_3:int) -> int:
    numero_mayor = 0
    #verifico que quede 1 si los 3 son iguales 
    if numero_1 == numero_2 and numero_1 == numero_3:
        numero_mayor = numero_1
        #ahora los comparo para averiguar cual es mayor
    elif numero_1 > numero_2 and numero_1 > numero_3:
        numero_mayor = numero_1
    elif numero_2 > numero_1 and numero_2 > numero_3:
        numero_mayor = numero_2 
    elif numero_3 > numero_1 and numero_3 > numero_2:
        numero_mayor = numero_3
        # si hay dos iguales y uno mayor 
    elif numero_1 == numero_2 and numero_1 > numero_3:
        numero_mayor = numero_1
    elif numero_2 == numero_1 and numero_2 > numero_3:
        numero_mayor = numero_2 
    elif numero_3 == numero_2 and numero_3 > numero_2:
        numero_mayor = numero_3
    elif numero_3 == numero_1 and numero_3 > numero_2:
        numero_mayor = numero_3
    elif numero_2 == numero_3 and numero_2 > numero_1:
        numero_mayor = numero_2
    return numero_mayor 



#MAXIMO NUMEROS PROMEDIO





#MOSTRAR DATOS 
def mostrar_datos(lista_a:list, lista_b:list, lista_c:list, lista_d:list):

    for i in range(len(lista_a)):

        if len(lista_a[i]) < 8:
            print("NOMBRE\t\tLEGAJO GENERO  \tNOTAS")
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}\t{lista_d[i]}")
        else:
            print("NOMBRE\t\tLEGAJO GENERO  \tNOTAS")
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}\t{lista_d[i]}")    


#COPIAR LISTA
def copiar_lista(lista_a:list, lista_b:list)->list:
    nombres_originales = [-1] * len(lista_a)
    edades_originales = [-1] * len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i] = lista_a[i]
        edades_originales[i] = lista_b[i]
    
    return nombres_originales, edades_originales

#ORDENAR ASCENDENTE
def ordenar_ascendente(lista_a:list, lista_b:list, lista_c:list)->list :

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
    lista_de_retorno = []
    for i in range(len(lista_a)):
        lista_de_retorno += [(lista_a[i], lista_b[i], lista_c[i])]
    
    return lista_de_retorno

#ORDENAR DESCENDENTE
def ordenar_descendente(lista_a:list, lista_b:list, lista_c:list)->list:

    for i in range(0, len(lista_a)-1, 1):  #empiezo desde 0 hasta el largo de la lista  -1 lugar (porque el último no tiene con quien comparar)
        
        for j in range(i + 1, len(lista_a), 1): # aca es lo inverso, j empieza desde i + 1 
            
            if lista_c[i] < lista_c[j]:
            
                edad_auxiliar = lista_b[i] #guardo lista b en edad auxiliar 
                lista_b[i] = lista_b[j]     # comparo las posiciones
                lista_b[j] = edad_auxiliar  #devuelvo el valor guardado de lista b 

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
    lista_de_retorno = []    
    for i in range(len(lista_a)):
        lista_de_retorno += [(lista_a[i], lista_b[i], lista_c[i])] #quiero guardar aca las 3 cosas para devolverlo por return
    
    return lista_de_retorno

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
                continue #cada vez que encuentro un dato valido, lo ignoro, la bandera igual arroja True
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


def validar_datos_edad(edad:int): #verifica si lo ingresado son numeros, devuelve True- False
    bandera = True   #devuelve true o false
    numero = ""
    for i in range(len(edad)):
        numero = ord(edad[i])  #guardo el numero ascii en "numero"
        if numero <= 48 or numero >= 57 :  # si no esta dentro de los numeros (0-9) arroja False
            bandera = False
            continue
    return bandera 



def validar_datos_legajo(legajo:str): #devuelve False si el numero tiene menos de 5 cifras o es una letra 
    bandera = True
    numero = ""
    for i in range(len(legajo)): 
        numero = ord(legajo[i])  #guardo el numero ascii en "numero"
        bandera = True
        if len(legajo) != 5: #verifico que el numero tenga 5 cifras de largo con "len"
            bandera = False 
            
        if numero < 48 or numero > 57: #Si esta fuera del rango 48 - 57 da False 
            bandera = False
            
    return bandera



def validar_datos_genero(genero:str):
    genero_guardado = ""
    bandera = False
    lista_de_validos = ['F', 'f', 'M', 'm', 'X', 'x']
    for i in lista_de_validos: #esto recorre la lista de validos 
        if genero == i: # comparo lo ingresado con la lista , i toma el valor de cada elemento de la lista en cada iteracion
            bandera = True   #cambia a True si coinciden
            
        if len(genero) >1: #Si lo ingresado es mas de 1 caracter, se mantiene en False 
            continue
                
    
    return bandera
    

'''
def buscar_vacio(lista:list)
    
    while True:
        notas = int(input("ingresar nota"))
        fila_vacia = -1    #busca una fila vacia, uso esto porque ninguna fila vacia vale -1 
        for i in range(len(matriz_magna)):
            if matriz_magna[i] == [0] * 5:
                fila_disponible = i   #guardo 


                
                break
                for j in range(len(matriz_magna[0])):
                    fila_marcela = notas
                    matriz_magna[i][j] = fila_marcela
                    print(fila_marcela)
        if contador_nota >= len(fila_marcela):
            print("no hay mas espacio")
            break

        respuesta = input("S para seguir cargando")
        if respuesta != "s":
            print(fila_marcela)
            break       
    '''


            
            


def ingresar_notas(nombres:str,matriz_magna:list)-> list:
    fila_alumnos = 0  #esto controla las filas a donde se ponen los datos , 0 = marcela, 1 = pepe ,2 Florencia etc
    contador_notas = 0

    for i in (matriz_magna): 
        for j in range(5): #(solo tengo que trabajar usando 5 columnas)
            nota = int(input(f"ingresar nota de lugar {j + 1}:  "))
            matriz_magna[fila_alumnos][j] = nota #guardo la nota ingresada en fila alumnos
            contador_notas +=1
            print(f"{nombres},{matriz_magna[fila_alumnos]}")
        if contador_notas == 5: #cuando el contador llega a 5 sale del bucle
            print("notas ingresadas correctamente. \n Fila completa")
            break
        
    return  matriz_magna


'''
# borrar esta mierda 


def ingresar_notas(nombre, fila_disponible):
    contador_notas = 0
    for j in range(5):
        nota = int(input(f"Ingresar nota {j + 1} para {nombre}: "))
        matriz_magna[fila_disponible][j] = nota
        contador_notas += 1
    print(f"Notas ingresadas para {nombre}: {matriz_magna[fila_disponible]}")
    print("Fila de notas completa")
    return fila_disponible + 1  # Devuelve la siguiente fila disponible




while True:
    nombres = input("Ingrese el nombre del alumno: ")
    
    match lower_propio(nombres):
        case "marcela" | "pepe" | "sofia" | "juan" | "ana" | "luis":  # etc., hasta 30 nombres
            fila_disponible = ingresar_notas(nombres, fila_disponible)
        
        case _:
            print("Nombre no reconocido.")

    segunda_vuelta = input("¿Desea ingresar notas para otro alumno?\n's' = sí\nOtra tecla = no\n> ")
    if segunda_vuelta.lower() != "s":
        break



 #pista ayuda para el promedio 
promedio = (variable_suma / cantidad_alumnos) * 10 // 1
        promedio = promedio / 10
yo hice eso para calcular la materia


'''







#MENU DE OPCIONES COMPLETO
def menu() -> int:
    while True:
        opcion_elegida = input("|--------------------------| Elige una opción: |--------------------------| \n"
            "1. Opción 1\n"
            "2. Opción 2\n"
            "3. Opción 3\n"
            "4. Opción 4\n"
            "5. Opción 5\n"
            "6. Opción 6\n"
            "7. Opción 7\n"
            "8. Salir\n"
            )
        
        match opcion_elegida:
            case "1":
                print("opción 1 asdasdad")
            case "2":
                print("opción 2")
            case "3":
                print("opción 3")
            case "4":
                print("opción 4")
            case "5":
                print("opción 5")
            case "6":
                print("opción 6")
            case "7":
                print("opción 7")
            case "8":
                print("Saliendo del programa")
                break
            case _:
                print("Opcion no valida, ingrese un numero dentro de los especificados.")

    return int(opcion_elegida)    

     
    





# FUNCION PROMEDIO 

def promedios_alumnos(matriz_magna:list)->list:
    promedios_guardados = []
   

    for i in matriz_magna:  #recorro las filas de la matriz con esto 
        contador_a = 0  #necesito poner suma y contador aca, dentro del for i, asi inician en 0 cada vez que itera y no me sobreescribe los datos
        suma_de_numeros = 0 
        for j in i: #recorro numero por numero dentro de las filas (j in i)
            suma_de_numeros += j  # aca guardo todo lo que recorre j en "suma_de_numeros"
            contador_a +=1 #siempre va a dar 5 
            
        promedio = suma_de_numeros / contador_a #guardo el numero en "promedio"
        promedios_guardados += [promedio] #lo sumo a la lista, para evitar que sobreescriba los resultados
            
   
    return promedios_guardados

#promedios por columna 
#llamada = promedios_alumnos(matriz_magna)
#print(llamada)



matriz_notas= [    [6,7,6,5,2],
                    [8,7,7,5,10],
                    [2,1,9,3,6],
                    [8,8,9,9,9],
                    [6,7,9,3,4],
                    [3,4,3,4,8],
                    [2,1,7,10,3],
                    [1,7,10,2,10],
                    [6,3,7,9,8],
                    [8,8,10,7,6],  #10
                    [1,7,5,9,5],
                    [9,4,3,4,7],
                    [3,4,6,3,1],
                    [7,5,5,3,1],
                    [2,5,3,3,4],
                    [5,10,1,5,1],
                    [5,6,8,2,3],
                    [3,9,10,3,7],
                    [6,5,9,7,9],
                    [3,2,10,2,5], #20
                    [3,9,4,3,1],
                    [8,5,4,7,9],
                    [1,6,4,2,10],
                    [10,7,10,3,9],
                    [4,7,2,1,3],
                    [1,2,6,1,8],
                    [10,10,4,3,3],
                    [8,8,1,8,2],
                    [8,4,1,8,9],
                    [6,5,1,2,2]] #30  

#PROMEDIOS POR COLUMNA 
def mostrar_promedio_por_columnas_general(matriz_notas:list)->list:
    resultado_1 = []
    for j in range(len(matriz_notas[0])): #recorro las columnas con este for
        suma_de_columnas = 0 
        for i in range(len(matriz_notas)): 
            suma_de_columnas += (matriz_notas[i][j]) #guardo los valores de las columnas, en este caso la primera en "suma de columnas"
        
        cuenta = (suma_de_columnas / len(matriz_notas)) #guardo la suma y la division en "cuenta", para sumarlo despues
        resultado_1 += [cuenta] # lo sumo a la lista final evitando que sobreescriba 
    
    return resultado_1
    


lista_promedios = mostrar_promedio_por_columnas_general(matriz_notas)
print(lista_promedios)

# averigua el numero mayor en listas
def el_mayor_en_listas(lista:list)-> list:
    numero_mayor = lista[0] 
    for i in range(0, len(lista)-1, 1):  
        for j in range(i + 1, len(lista), 1):
            if lista[i] > lista[j]:
                numero_mayor = lista[i]

    return numero_mayor

llamar = el_mayor_en_listas(lista_promedios)
print(llamar)
