for i in range(4, 101, 4):
    print(i)


//////////////////////////////////////////////////////////////////


lista = ["pizza", "mate", "fútbol", "dormir", "viajes"]
print(lista[-2])


//////////////////////////////////////////////////////////////////


lista = []
lista.append("python")
lista.append("guitarra")
lista.append("viaje")
print(lista)


//////////////////////////////////////////////////////////////////


animales = ["perro", "gato", "tigre", "elefante"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)


//////////////////////////////////////////////////////////////////


# Crea una lista llamada numeros con 5 elementos diferentes, encuentra el valor maximo de ellos y lo elimina 
# por ultimo muestra la lista sin ese valor maximo en este caso seria (22) 


//////////////////////////////////////////////////////////////////


numeros = list(range(10, 31, 5))
print(numeros[:2])


//////////////////////////////////////////////////////////////////


autos = ["Ford", "Chevrolet", "Toyota", "Honda"]
autos[1:3] = ["Renault", "Audi"]
print(autos)


//////////////////////////////////////////////////////////////////


dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


//////////////////////////////////////////////////////////////////


compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

compras[0].remove("pan")

print(compras)


//////////////////////////////////////////////////////////////////


lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)


//////////////////////////////////////////////////////////////////