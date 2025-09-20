# Se puede usar el random.uniform para crear 10 numeros decimales aleatorios si lo quiero asi 

# import random
# notas = [round(random.uniform(1, 10), 2) for _ in range(10)]

notas = [7.5, 8.0, 6.5, 9.0, 5.5, 10.0, 4.0, 8.5, 6.0, 7.0]
print("Notas de los estudiantes:", notas)
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)
nota_max = max(notas)
nota_min = min(notas)
print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)


//////////////////////////////////////////////////////////////////


productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

productos_ordenados = sorted(productos)
print("Lista de productos ordenados alfabéticamente:")
print(productos_ordenados)

eliminar = input("Ingrese el producto que desea eliminar: ")

if eliminar in productos_ordenados:
    indice = productos_ordenados.index(eliminar)
    del productos_ordenados[indice]  
    print("Lista actualizada de productos:")
    print(productos_ordenados)
else:
    print("El producto no se encuentra en la lista.")


//////////////////////////////////////////////////////////////////


import random

numeros = [random.randint(1,100)for _ in range(15)]
print (f"Lista completa:{numeros}")

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print (f"Lista de pares:{pares}")
print ("Cantidad de pares:", len(pares))


//////////////////////////////////////////////////////////////////


lista1 = [1,3,5,3,7,1,9,5,3]
lista2 = []

lista2 = lista1[0:1]

for i in range (len(lista1)):
    if lista1[i] not in lista2:
        lista2.append(lista1[i])

print (lista2)


//////////////////////////////////////////////////////////////////


estudiantes = ["Ana", "Luis", "María", "Pedro", "Sofía", "Juan", "Carla", "Diego"]

print("Lista inicial de estudiantes:")
print(estudiantes)

opcion = input("¿Desea agregar un nuevo estudiante o eliminar uno existente? (agregar/eliminar): ").lower()

if opcion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print("Estudiante agregado.")

elif opcion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print("Estudiante eliminado.")
    else:
        print("Ese estudiante no está en la lista.")

else:
    print("Opción no válida.")

print("Lista final de estudiantes:")
print(estudiantes)


//////////////////////////////////////////////////////////////////


numeros = [10, 20, 30, 40, 50, 60, 70]

ultimo = numeros[-1]          
numeros[1:] = numeros[:-1]    
numeros[0] = ultimo           

print("Lista rotada:", numeros)


//////////////////////////////////////////////////////////////////


temperaturas = [
    [12, 22],
    [14, 25],
    [11, 23],
    [13, 26],
    [15, 28],
    [10, 24],
    [12, 27]
]

minimas = [temp[0] for temp in temperaturas]
maximas = [temp[1] for temp in temperaturas]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

print("Promedio de temperaturas mínimas:", round(promedio_min, 2))
print("Promedio de temperaturas máximas:", round(promedio_max, 2))

amplitudes = [temp[1] - temp[0] for temp in temperaturas]

mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud) + 1

print("Mayor amplitud térmica:", mayor_amplitud)
print("Se registró en el día:", dia_mayor_amplitud)


//////////////////////////////////////////////////////////////////


notas = [
    [7, 8, 9],   # Estudiante 1
    [6, 7, 8],   #     "      2
    [9, 9, 10],  #     "      3
    [5, 6, 7],   #     "      4 
    [8, 7, 6]    #     "      5
]

print("Promedio de cada estudiante:")
for i, estudiante in enumerate(notas, start=1):
    promedio_est = sum(estudiante) / len(estudiante)
    print("Estudiante", i, ":", round(promedio_est, 2))

print("Promedio de cada materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    suma_materia = sum(notas[i][j] for i in range(len(notas)))
    promedio_materia = suma_materia / len(notas)
    print("Materia", j+1, ":", round(promedio_materia, 2))
    
    
//////////////////////////////////////////////////////////////////


tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(fila)

for turno in range(9): 
    mostrar_tablero()
    
    jugador = "X" if turno % 2 == 0 else "O"
    print("Turno del jugador", jugador)
    
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, intente de nuevo")
        turno -= 1

print("Tablero final:")
mostrar_tablero()


//////////////////////////////////////////////////////////////////


ventas = [
    [10, 12, 11, 14, 13, 15, 10],  # Producto 1
    [5, 8, 6, 7, 5, 9, 6],         #    "     2
    [20, 18, 22, 19, 21, 20, 23],  #    "     3
    [7, 6, 5, 8, 7, 6, 7]          #    "     4
]

print("Total vendido por cada producto:")
total_productos = []
for i in range(4): 
    total = 0
    for j in range(7):  
        total += ventas[i][j]
    total_productos.append(total)
    print("Producto", i+1, ":", total)

totales_dias = []
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    totales_dias.append(total_dia)

mayor = totales_dias[0]
dia = 1
for k in range(7):
    if totales_dias[k] > mayor:
        mayor = totales_dias[k]
        dia = k+1
print(f"Día con mayores ventas totales: Día {dia}")

mayor_prod = total_productos[0]
prod = 1
for i in range(4):
    if total_productos[i] > mayor_prod:
        mayor_prod = total_productos[i]
        prod = i+1
print(f"Producto más vendido en la semana: Producto {prod}")


//////////////////////////////////////////////////////////////////