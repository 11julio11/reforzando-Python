from gestion_productos import productos

def buscar_producto(nombre):
    nombre = nombre.lower()
    for producto in productos:
        if producto['nombre'].lower() == nombre:
           return f"Producto encontrado: {producto['nombre']}, Precio: ${producto['precio']}"
    return "Producto no encontrado."

         
         
