#Matias San Pedro Integrador Validaciones 
'''
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.

'''
apellido = input("Ingrese Apellido \n")
edad = int(input("Ingrese Edad \n"))
estado_civil = input("ingrese Estado Civil \n")
numero_de_legajo = int(input("ingrese numero de legajo \n"))
marca_de_estados = 0  #0 = estado inicial | 1 = validado | 2 = incorrecto


#edad
while edad > 90 or edad < 18:
    edad = int(input("edad incorrecta, ingrese un numero entre 18 y 90 "))
#estado civil
while marca_de_estados != 1:
    match estado_civil:
        case "soltero":
            marca_de_estados = 1
        case "casado":
            marca_de_estados = 1
        case "divorciado":
            marca_de_estados = 1
        case "viudo":
           marca_de_estados = 1
        case _: 
            marca_de_estados = 2
           
    if marca_de_estados == 1:
        print("estado civil validado")
    if marca_de_estados == 2:
        print("estado civil no validado")
        estado_civil = input("vuelva a ingresar estado civil \n")
#legajo
while numero_de_legajo > 9999 or numero_de_legajo < 1000:
    numero_de_legajo = int(input("legajo incorrecto, ingreselo nuevamente \n"))

print(f"los datos validados son: \n apellido :{apellido} \n edad: {edad} \n estado civil: {estado_civil} \n legajo: {numero_de_legajo}")