edad: int = int(input("Ingrese por pantalla su edad: "))

if edad >= 18: 
    print("Es mayor de edad")


///////////////////////////////////////////////////////////////////////////////

nota: int = int(input("Ingrese su nota en pantalla: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    

///////////////////////////////////////////////////////////////////////////////


num_par: int = int(input("Ingrese un numero par por pantalla: "))

if num_par % 2 == 0 : 
    print("Ha ingresado un numero par")
else:
    print("Porfavor, ingrese un numero par")
    
    
///////////////////////////////////////////////////////////////////////////////


edad: int = int(input("Ingrese su edad por pantalla: "))

if edad < 12 and edad > 0:
    print("Es un/a niño/a")
elif edad >= 12 and edad < 18:
    print("Es un/a adolescente")
elif edad >= 18 and edad < 30:
    print("Es un/a adulto/a joven")
else:
    print("Es un adulto/a")
    
    
///////////////////////////////////////////////////////////////////////////////


contraseña = input("Ingrese su contraseña: ")

if len(contraseña) <= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
    
///////////////////////////////////////////////////////////////////////////////


import statistics
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)] 

media = statistics.mean (numeros_aleatorios)
mediana = statistics.median (numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)
 
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if isinstance(moda, str):
    if media > mediana:
        print("Sesgo positivo (asimetría a la derecha)")
    elif media < mediana:
        print("Sesgo negativo (asimetría a la izquierda)")
    else:
        print("No hay sesgo (asimetría nula)")


///////////////////////////////////////////////////////////////////////////////


frase: str = str(input("Ingrese una frase o palabra por pantalla: "))

vocales = "aeiouAEIOU"
if frase[-1] in vocales:
    frase += "!"
    
print(frase)


///////////////////////////////////////////////////////////////////////////////


nombre: str = str(input("Ingrese su nombre: "))

print ("Elija como quiere que se imprima su nombre en pantalla: ")
print ("1) Su nombre se escribira en MAYUSCULAS")
print ("2) Su nombre se escribira en minusculas")
print ("3) Su nombre se escribira en con la primer letra en mayuscula")

opcion = int = int(input("Ingrese 1, 2 o 3: "))

if opcion == 1:
    print (nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.capitalize())
else:
    print("Opcion no valida")


///////////////////////////////////////////////////////////////////////////////


magnitud: float = float(input("Ingrese la magnitud del terremoto: "))

if magnitud >= 1 and magnitud < 3:
    print("Muy Leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
elif magnitud >= 7 and magnitud < 10:
    print("Extremo!!")
else:
    print("Magnitud no valida")


///////////////////////////////////////////////////////////////////////////////


hemisferio: str = str(input("¿En qué hemisferio se encuentra? (N/S): ")).upper()
mes: int = int(input("Ingrese el mes en el que se encuentra (1-12): "))
dia: int = int(input("Ingrese el día en el que se encuentra (1-31): "))

estacion = ""

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        estacion = "Otoño"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"Usted se encuentra en {estacion}!")


///////////////////////////////////////////////////////////////////////////////