#otro ayuda para calculadora 

operacion = input("Elige: suma | resta | division | multiplicacion : ").lower()

while operacion != "suma" and operacion != "resta" and operacion != "division" and operacion != "multiplicacion":
    operacion= input("ERROR!! ingrese una operacion valida : " )
 
a = input("Elegi el primer numero: ")
a = int(a)

b = input("Elegi el segundo numero: ")
b = int(b)

def suma_calculadora (a , b):
    sumar = a + b
    return sumar
    
def resta_calculadora (a , b):
    restar = a - b
    return restar
        
def division_calculadora (a , b):
    dividir = a / b
    return dividir
    
def multiplicacion_calculadora (a , b):
    multiplicar = a * b
    return multiplicar

match operacion:
    case "suma":
        resultado_suma = suma_calculadora(a , b)
        print(resultado_suma)
    case "resta":
        resultado_resta = resta_calculadora(a , b)
        print(resultado_resta)
    case "division":
        if b == 0:
           b = print("No se puede dividir por cero : ")
        else:
             resultado_division = division_calculadora (a , b)
             print(resultado_division)
    case "multiplicacion":
        resultado_multiplicacion = multiplicacion_calculadora(a , b)
        print(resultado_multiplicacion)