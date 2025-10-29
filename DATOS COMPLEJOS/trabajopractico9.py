precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)


///////////////////////////////////////////////////////////////////////


precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)


///////////////////////////////////////////////////////////////////////


frutas = list(precios_frutas.keys())
print(frutas)


///////////////////////////////////////////////////////////////////////


telefonos = {}
for i in range(5):
    nombre = input("Nombre: ")
    numero = input("Número: ")
    telefonos[nombre] = numero
consulta = input("Consultar nombre: ")
if consulta in telefonos:
    print("Número:", telefonos[consulta])
else:
    print("No encontrado")


///////////////////////////////////////////////////////////////////////


frase = input("Frase: ")
palabras = frase.lower().split()
unicas = set(palabras)
print(unicas)
contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1
print(contador)


///////////////////////////////////////////////////////////////////////


alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Nota {j+1}: ")) for j in range(3))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas)/len(notas)
    print(nombre, promedio)


///////////////////////////////////////////////////////////////////////


parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}
print("Ambos:", parcial1 & parcial2)
print("Solo uno:", parcial1 ^ parcial2)
print("Al menos uno:", parcial1 | parcial2)


///////////////////////////////////////////////////////////////////////


stock = {}
while True:
    opcion = input("Consultar/Agregar/Salir: ").lower()
    if opcion == "salir":
        break
    producto = input("Producto: ")
    if opcion == "consultar":
        print(stock.get(producto, "No existe"))
    elif opcion == "agregar":
        unidades = int(input("Unidades: "))
        if producto in stock:
            stock[producto] += unidades
        else:
            stock[producto] = unidades
    print(stock)


///////////////////////////////////////////////////////////////////////


agenda = {}
while True:
    opcion = input("Agregar/Consultar/Salir: ").lower()
    if opcion == "salir":
        break
    dia = input("Día: ")
    hora = input("Hora: ")
    clave = (dia, hora)
    if opcion == "agregar":
        evento = input("Evento: ")
        agenda[clave] = evento
    elif opcion == "consultar":
        print(agenda.get(clave, "Sin actividad"))


///////////////////////////////////////////////////////////////////////


paises = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Uruguay': 'Montevideo'}
capitales = {v: k for k, v in paises.items()}
print(capitales)


///////////////////////////////////////////////////////////////////////