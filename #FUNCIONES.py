#FUNCIONES 

'''1 )Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def numero_entero () ->int :
    num = input("Numero entero")
    return num 

    #llamado a la funcion:
funcion = numero_entero()   
print(funcion)
#######################


#2)
#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def numero_flotante() ->float :
    num = input("Numero flotante")
    return num 

funcion = numero_flotante() #llamado a la funcion
print(funcion)

##########################

3)
Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.


def cadena ():
    chain = input("ingresar texto")
    return chain 

funcion_cadena = cadena()
print(funcion_cadena)
##############################

4)
Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área


def area_de_rectangulo()-> int:
    base = int(input("ingresar base"))        #pido los datos necesarios
    altura = int(input("ingresar altura"))
    area = (base * altura)    #multiplico base por altura y devuelvo ese numero como retorno
    return area


llamada = area_de_rectangulo() #llamo a la funcion 
print(f"el area de nuestro rectángulo es {llamada}")

###############################################


5)   Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.


def area_de_circulo()-> float:
    radio = float(input("ingrese radio ")) #pido el radio
    resultado_area =   3.14  * (radio * radio )   #pi por radio al cuadrado
    return resultado_area      #retorno el resultado de la cuenta 

llama = area_de_circulo()    #llamo a la funcion
print (f"el area del circulo es : {llama}")

#########################################################


6) Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.


def par () -> int:
    numeros = int(input("ingresar numero"))  #pido un numero 

 #aplico las condiciones para verificar que sea par o impar 
    if numeros % 2 == 0:
        print("el numero ingresado es par")
    if numeros % 2 == 1:
        print("el numero ingresado es impar")
    
    
Llamada = par()  #llamo a la funcion

##################################################



8) Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande


def maximo () -> int:
    numero_1 = int(input("ingresar numero 1 "))
    numero_2 = int(input("ingresar numero 2 "))
    numero_3= int(input("ingresar numero 3 "))
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
    
max = maximo()
print(f"el mayor numero ingresado es {max}")
################################################

9) Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potencia() -> int:
    base = int(input("BASE: "))
    exponente = int(input("EXPONENTE"))
    result = base ** exponente
    return result

pot = potencia()
print (pot)

#########################################

10) Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.




def primo()->bool:
    valor_retorno = True
    dato = int(input("ingresar un numero"))
    for i in range(2, dato):  
        if dato % i == 0:
            valor_retorno = False
            break
    return valor_retorno
pr = primo()

print(pr)

11)
Crear una función que (utilizando el algoritmo del ejercicio de la guia de for),
 muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro.
   La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.


def hallar_primos(numero) -> int:   

    for p in range(1, numero + 1):  #recorro desde el 1 hasta mi numero
        if p  == 1:
            continue  # Excluyo 1, no es primo

        primo = True  # Bandera para detener la iteracion
        for i in range(2, p):   #recorro desde el dos hasta mi numero 
            if p % i == 0:  # este modulo me detecta los que no son primos, busca divisores de p
                primo = False    #esta bandera cambia cuando el if encuentra un divisor 
                break

        if primo == True:  
            print(f"{p} es primo")

      
numero = int(input("Ingresá un número: "))
hallar_primos(numero)  
#########################################







12)
Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro.
 La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación.
 Por defecto es del 1 al 10.

'''


numero1 = int(input("ingresar el primer numero, ingrese 0 para mostrar la tabla por defecto \n "))
contador = 1

if numero1 == 0:
    for i in range(1,11): 
        print(f"{1 * i }")

else:
    for b in range(1,11):
        multiplicacion = (numero1 * b)
        print(multiplicacion)




   

    
    
        
    
    
    

#inicio = int(input("desde que numero quiere empezar? "))
#fin =int(input("en que numero desea terminar? "))





