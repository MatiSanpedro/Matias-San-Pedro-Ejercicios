# EJERCICIOS FOR

#1) mostrar los numeros de forma ascendente del 1 al 10
'''
for i in range (1,11):
    print (i)

       
#############################################################
#2) mostrar los numeros de forma descendente del 10 al 1 
for i in range(10,0,-1):
    print(i)

###################################################    
    '''
'''
#3) Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
numero = int(input("insertar numero"))
for i in range(0,numero):
    i += 1
    print(i)
################################################
'''
#4) Ingresar un número y mostrar la tabla de multiplicar de ese número.
#  Por ejemplo si se ingresa el numero 5:

#	5 x 0 = 0
#	5 x 2 = 10
#	5 x 3  = 15 
'''
numero = int(input("insertar numero"))
for i in range(1,11):
    tabla = numero * i 
    print (tabla)
    ######################################
    '''
#5) Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0.
#  Mostrar la suma y el promedio de todos los números.
'''
acumulador = 0
contador = 0

for i in range (1,11):
    numeros = int(input("ingresar numeros, ingrese 0 para finalizar \n"))
    contador +=1
    acumulador += numeros 
     
    if numeros == 0:
        contador -=1
    
        break
    if numeros != 0:
        promedio = acumulador / contador

print (f"{contador},{acumulador},{promedio }, {numeros}")
################################

#6) Imprimir los números múltiplos de 3 entre el 1 y el 10

for i in range(0,11,3):
    print(i)
###################################    
  

#7) Mostrar los números pares que hay desde la unidad hasta el número 50. 

for i in range (0,51,2):
    print(i)
 
#########################################
Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
'''
'''
# 8) 
ingreso = int(input("Ingresar numero"))
ingresobis = ingreso + 6 
lista = []                #lista vacia 
for i in range(ingreso, ingresobis):   #el punto de partida de la iteracion es el numero que yo ingreso, el limite  es el mismo numero 5 lugares mas arriba
    lista.append(i)       # append agrega elementos al final de mi lista, yo le agrego todo "i" 
    print (f"{lista}")
    '''
##################################
'''  
#9) Ingresar un número.
#  Mostrar todos los divisores que hay desde el 1 hasta el número ingresado.
#  Mostrar la cantidad de divisores encontrados.

numero = int(input("venga el numero \n"))
for i in range (1, numero):
    division = numero % i
    if division == 0:
        print(f"{i}")
  ###########################################
''' 
'''   
#10) Ingresar un número. Determinar si el número es primo o no 

for i in range (1, 10):
    numero = int(input("venga el numero \n"))
    if numero % i  == 0:
        print(f"{numero} no es primo \n")
    
    else:
        print(f"{numero}  es primo")

#########################################


11) Ingresar un número.
 Mostrar cada número primo que hay entre el 1 y el número ingresado.
Informar cuántos números primos se encontraron.

  

numero = int(input("Ingrese un número: "))

for p in range(1, numero + 1):
    if p <= 1:
        continue  

    primo = True  

    for i in range(2, p):
        if p % i == 0:
            primo = False
            break

    if primo:
        print(f"{p} es primo")

'''
