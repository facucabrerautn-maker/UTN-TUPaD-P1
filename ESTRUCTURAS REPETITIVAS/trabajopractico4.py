num: int = 0
for i in range(1,101):
    print(i)
    
    
///////////////////////////////////////////////////////////////////////////


num : int = int(input("Ingrese un numero entero aleatorio: "))
n = abs(num)
if n == 0 :
    cantidad_digitos=1   
else:
    cantidad_digitos= 0
    for _ in str(n):
        cantidad_digitos += 1

print(f"El numero {num} tiene {cantidad_digitos} digito(s).")


///////////////////////////////////////////////////////////////////////////


num1 : int =int(input("Ingrese el primer numero: "))
num2 : int =int(input("Ingrese el segundo numero: "))

menor = min(num1,num2)
mayor = max(num1,num2)

suma = 0


for i in range(num1+1,num2):
    suma += i
    
print(f"La suma de todos los numeros enteros entre {num1} y {num2} es {suma}")


///////////////////////////////////////////////////////////////////////////


bandera : bool = True
suma: int = 0 

while bandera:
    numero: int=int(input("Ingrese el numero que quiere sumar en secuencia: "))
    suma += numero
    if numero == 0:
        bandera = False
print(f"El resultado final es: {suma}")


///////////////////////////////////////////////////////////////////////////
    
    
import random
num_secreto = random.randint(0,9)
intentos = 0

print("Adivina el numero aleatorio entre 0 y 9")

while True:
    intento = int(input("Ingresa un numero: "))
    intentos += 1
    if intento == num_secreto:
        print("¡Felicidades has encontrado el numero aleatorio!")
        print(f"La cantidad de intentos requeridos fueron {intentos}")
        break
    else:
        print("Numero incorrecto, intenta otra vez: ")
        
        
///////////////////////////////////////////////////////////////////////////


for i in range (100,-1,-2):
    print (i)


///////////////////////////////////////////////////////////////////////////


num : int=int(input("Ingrese un numero entero positivo: "))
suma=0
for i in range(num+1):
    suma += i

print(f"La suma de todos los numeros entre el 0 y {num} es: {suma}")


///////////////////////////////////////////////////////////////////////////


pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(1, 11): #for i in range(1, 101):
    numero = int(input(f"Ingrese el número {i}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
        
print("\n--- RESULTADOS ---")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


///////////////////////////////////////////////////////////////////////////


cantidad = 10   #simplemente cambiar a 100

suma = 0

for i in range(1, cantidad + 1):
    numero = int(input(f"Ingrese el número {i}: "))
    suma += numero

media = suma / cantidad

print("\n--- RESULTADO ---")
print(f"La media de los {cantidad} números es: {media}")


///////////////////////////////////////////////////////////////////////////


numero = int(input("Ingrese un número entero: "))

invertido = int(str(numero)[::-1])

print(f"El número invertido es: {invertido}")


///////////////////////////////////////////////////////////////////////////



