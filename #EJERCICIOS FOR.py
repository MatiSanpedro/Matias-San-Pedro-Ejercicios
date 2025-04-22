#EJERCICIOS FOR
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
acumulador = 0

for iteraciones in range (1,11):
    numeros = int(input("ingresar numeros, ingrese 0 para finalizar \n"))
    
    acumulador += numeros 
    if numeros == 0:
        contador = iteraciones - 1
        print (f"{iteraciones}, {numeros}, {acumulador}, {contador}")
        break
    

'''
ejecucion = True
while ejecucion == True:
    ingreso = int(input("venga el numero"))
    contador += 1
    if contador == 10 or ingreso == 0:
        ejecucion = False 
        '''