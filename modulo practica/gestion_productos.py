'''
1. Agregar productos a una lista
Crea un programa que permita al usuario agregar productos (nombre y precio) a una lista y luego muestre todos los productos agregados.
'''

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
