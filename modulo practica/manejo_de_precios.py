from gestion_productos import productos

def mostrar_precios():
    if productos:
        print("\nLista de precios:")
        for producto in productos:
            print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}")
        else:
            print("no hay productos en la lista.")    