def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    print(f"Factorial de {i}: {factorial(i)}")

//////////////////////////////////////////////////////////////////

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición para la serie de Fibonacci: "))

for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
print()

//////////////////////////////////////////////////////////////////

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
print(potencia(base, exp))

//////////////////////////////////////////////////////////////////

def a_binario(n):
    if n < 2:
        return str(n)
    else:
        return a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))
print(a_binario(numero))

//////////////////////////////////////////////////////////////////

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print(es_palindromo(texto))

//////////////////////////////////////////////////////////////////

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número para sumar sus dígitos: "))
print(suma_digitos(numero))

//////////////////////////////////////////////////////////////////

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques en la base: "))
print(contar_bloques(niveles))

//////////////////////////////////////////////////////////////////

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    contador = 1 if ultimo_digito == digito else 0
    
    return contador + contar_digito(numero // 10, digito)

num = int(input("Ingrese el número: "))
dig = int(input("Ingrese el dígito a buscar: "))
print(contar_digito(num, dig))

//////////////////////////////////////////////////////////////////

#Costo bastante hacerlo a pesar de ser basico