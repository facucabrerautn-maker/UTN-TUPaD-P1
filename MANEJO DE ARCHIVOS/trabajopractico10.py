def leer_productos(nombre_archivo):
    productos = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    except FileNotFoundError:
        with open(nombre_archivo, "w", encoding="utf-8"):
            pass
    return productos


def mostrar_productos(productos):
    if not productos:
        print("No hay productos cargados.")
    else:
        for p in productos:
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def agregar_producto(nombre_archivo, productos):
    nombre = input("Ingrese el nombre del nuevo producto: ").strip()
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo)

    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado correctamente.")


def buscar_producto(productos):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto encontrado -> Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")


def guardar_productos(nombre_archivo, productos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Productos guardados correctamente.")


def main():
    nombre_archivo = "productos.txt"
    productos = leer_productos(nombre_archivo)

    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Buscar producto")
        print("4. Guardar y salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            agregar_producto(nombre_archivo, productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            guardar_productos(nombre_archivo, productos)
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()

#  ¿Se puede agregar más de un producto?
#  Si se puede agregar mas de un producto, aunque deja escribir numeros como nombre del producto por ej: Nombre: 300, Precio: 300, Cantidad: 50

#  ¿Se guarda todo correctamente?
#  Se guarda todo completamente sin errores en el listado

#  ¿Se muestra bien el resultado?
#  El resultado se muestra claro y bien remarcadas las diferencias entre el nombre, precio y cantidad como el ejemplo del trabajo esta separado  por | (barras)