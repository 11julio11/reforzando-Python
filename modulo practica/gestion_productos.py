productos = []

def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input(f"Ingresa el precio de {nombre}: "))
    productos.append({'nombre': nombre, 'precio': precio})
    print(f"Producto {nombre} agregado exitosamente.")

def listar_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}")
    else:
        print("No hay productos en la lista.")
