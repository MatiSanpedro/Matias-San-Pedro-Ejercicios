#matrices 
# realizar una funcion que haga una suma de matrices 
'''
#esta la hice yo 
matriz1 = [[1,3,5],
            [5,7,5]]
matriz2 = [[2,4,6],
            [6,8,9]]

def suma_de_matrices(matriz1:list,matriz2:list)->list:
    resultado = [[0,0,0],
            [0,0,0]]
    for filas in range(len(matriz1)):
        for columnas in range(len(matriz2[filas])):
            resultado[filas][columnas] = matriz1[filas][columnas] + matriz2[filas][columnas]
            
            
    return resultado

llamada = suma_de_matrices (matriz1,matriz2)
print(llamada)

############################
#esto es de un compañero 



Inicializar matriz
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

suma de matriz
def sumar_matriz(matriz_uno:list, matriz_dos:list) -> list:
    matriz_resultado = inicializar_matriz(len(matriz_uno), len(matriz_uno[0]), 0)
    for i in range(len(matriz_uno)):
        for j in range(len(matriz_uno[i])):
            matriz_resultado[i][j] = matriz_uno[i][j] + matriz_dos[i][j]
    return matriz_resultado


Escalar de una matriz
def escalar_matriz(matriz_uno:list, escalar:int) -> list:
    matriz_resultado = inicializar_matriz(len(matriz_uno), len(matriz_uno[0]), 0)
    for i in range(len(matriz_uno)):
        for j in range(len(matriz_uno[i])):
            matriz_resultado[i][j] = matriz_uno[i][j] * escalar
    return matriz_resultado


matriz_uno = [[2,3],
              [4,5]]
#matriz_dos = [[2,5],
#              [8,7]]

for i in range(len(matriz_uno)):
    print(matriz_uno[i])
    
matriz_rtdo = escalar_matriz(matriz_uno,5)

for i in range(len(matriz_rtdo)):
    print(matriz_rtdo[i])



'''



# esto es de un compañero 

matriz3 = [[4,6],
           [8,10]]

#funcion que multiplique matriz por escalar
#funcion que haga la suma de las multiplicaciones

# palindromo, retorna true o false segun el caso
'''
def palindromo(palabra1:str)->bool:
    es_palindromo = True
    for i in range(len(palabra)):
        if palabra[i]!= palabra[(len(palabra)-1)-i]:
            
            es_palindromo = False
            break
    return es_palindromo



def palindromo(palabra:str)->bool:
    es_palindromo = True
    for i in range(len(palabra)):
        if palabra[i] != palabra[(len(palabra)-1) -i]:
            es_palindromo = False
            break

    return es_palindromo
#esto esta incompleto

#preguntar por que se usan los indices [i] cuando se realizan 
#operaciones

#Realizar una funcion que multiplique dos matrices y devuelva una nueva matriz.
# # # # # # # # # # # # # # # # # # # # # 




#Las matrices solo de pueden multiplicar cuando i x k <-> k x j donde: 
# i es la cantidad de filas de la primera matriz.
# k es la cantidad de columnas de la primera matriz.
# k es la cantidad de filas de la segunda matriz.
# j es la cantidad de columnas de la segunda matriz.
# el resultado de la multiplicacion es una matriz de i x j.

#Inicializar matriz
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz
matriz_3 = [[5,0,3], [3,2,5]] #Columnas de este
matriz_4 = [[2,1], [0,3], [4,6]] #Filas de este



def multiplicar_matrices(matriz_a:list, matriz_b:list) -> list:
    if len(matriz_a[0]) != len(matriz_b): #Verificacion de que las matrices se pueden multiplicar
        return "Las matrices no se pueden multiplicar"        #cambiar esto, la funcion tiene que tener solamente un retorno 
    matriz_c = inicializar_matriz(len(matriz_a), len(matriz_b[0]), 0) #Inicializa una matriz i x j vacia
    for i in range(len(matriz_a)): #Recorre las filas de la matriz_a
        for j in range(len(matriz_b[0])): #Recorre las columnas de la matriz_b
            for k in range(len(matriz_b)): 
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j] 
    return matriz_c

probando = multiplicar_matrices(matriz_3, matriz_4) 

'''

cadena = "repetir"
