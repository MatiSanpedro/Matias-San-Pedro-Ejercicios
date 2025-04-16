#ejercicio de calculadora, es una ayuda

#este es el mas bueno 
def sumar (a,b):
    """
    Suma dos numeros. 
    
    Retorna el resultado de la suma

    """
    return a + b

def restar (a, b):
    """
    Resta dos numeros. 
    
    Retorna el resultado de la resta

    """
    return a - b

def multiplicar(a, b):
    """
    Multiplica dos numeros. 
    
    Retorna el resultado de la multiplicacion

    """    
    return a * b 

def dividir(a, b):
    """
    Divide dos numeros. 
    
    Retorna el resultado de la division

    """    
    return a / b







def calculador():
    
    flag = True
    
    print("---------------------------------------------MENU--------------------------------------------------")
    
    eleccion_usuario = input("¿Que operacion desea realizar:\n a) Sumar.\n b) Restar.\n c) Multiplicar.\n d) Dividir.\n")
    while not eleccion_usuario:
        print("Error, ingrese una opcion...\n")
        eleccion_usuario = input("¿Que operacion desea realizar:\n a) Sumar.\n b) Restar.\n c) Multiplicar.\n d) Dividir.\n")

        
    numero_uno = int(input("Ingrese el primer numero: "))
    numero_dos = int(input("Ingrese el segundo numero: "))
    
    match eleccion_usuario:
        case "a":
            resultado = sumar (numero_uno, numero_dos)
            
        case "b":
            resultado = restar (numero_uno, numero_dos)
            
        case "c": 
            resultado = multiplicar(numero_uno, numero_dos)
            
        case "d":
            if numero_dos == 0:
                print("No se puede dividir con cero")
            else:
                resultado = dividir(numero_uno, numero_dos)
        case "e":
            continuar = False
            
        case _:
            print("OPCION INCORRECTA.\n")
            flag = False
            
    if flag == True:   
        print(f"\nEl resultado de la operacion es: {resultado}")  
        
            
while True:
    calculador()
    pregunta = input("Desea realizar otra operacion? (si,no): ")
    if pregunta == "no":
        break
    else:
        calculador()

