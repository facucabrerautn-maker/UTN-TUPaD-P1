print("Hola Mundo")

//////////////////////////////////////////////////////////////////

nombre = input("Ingresa tu nombre: ")
print(f"¡Hola {nombre}!")

//////////////////////////////////////////////////////////////////

nombre_completo=input("Ingrese su nombre completo por pantalla: ")
edad=input("Ingrese su edad a continuacion: ")
lugar_de_residencia=input("Ingrese su lugar de residencia actualmente: ")
print(f"Soy {nombre_completo},tengo {edad} y vivo en {lugar_de_residencia}")

//////////////////////////////////////////////////////////////////

radio: float = float(input("Ingrese el radio de un circulo: "))
area: float = 3.14 * (radio**2)
perimetro: float =  2 * 3.14 * radio
print(f"El area del circulo es: {area} y su perimetro es: {perimetro} ")

//////////////////////////////////////////////////////////////////

segundos: int = int(input(" Ingrese por pantalla una cantidad de segundos aleatoria: "))
horas: float = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

//////////////////////////////////////////////////////////////////

numero: int = int(input("Ingrese por pantalla un numero para ver su tabla de multiplicar: "))
resultado: int

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

//////////////////////////////////////////////////////////////////

numero1: int = int(input(" Ingrese un numero entero distinto de 0(cero) "))
numero2: int = int(input(" Ingrese otro numero entero distinto de 0(cero)" ))
suma: int = numero1 + numero2
resta: int = numero1 - numero2
division: float = numero1 / numero2
multiplicacion: int = numero1 * numero2
print(f""" 
      La suma de los dos numeros es: {suma}
      La resta de los numeros es: {resta}
      La division de los dos numeros es: {division}
      La multiplicacion de los dos numeros es: {multiplicacion}""")

//////////////////////////////////////////////////////////////////

altura: float = float(input(" Ingrese su altura a continuacion: "))
peso: float = float(input(" Ingrese su peso a continuacion: "))
imc: float = peso / (altura**altura)
print(f" Su indice de masa corporal es: {imc} ")

//////////////////////////////////////////////////////////////////

celsius: float = float(input(" Ingrese la temperatura en Celsius que desea convertir a Fahrenheit "))
fheit: float = (celsius * 9/5 + 32)
print(f"La equivalencia de {celsius} C° a Fahrenheit es: {fheit} F° ")

//////////////////////////////////////////////////////////////////

numero1: float = float(input( " Ingrese el primer numero: "))
numero2: float = float(input( " Ingrese el segundo numero: "))
numero3: float = float(input( " Ingrese el tercer numero: "))
promedio: float = (numero1 + numero2 + numero3) / 3
print(f" El promedio de los 3 numeros ingresados es de: {promedio} ")
    
//////////////////////////////////////////////////////////////////