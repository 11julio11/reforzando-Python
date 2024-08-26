# main.py
from gestion_productos import agregar_producto, listar_productos
from buscar_producto import buscar_producto

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar un producto")
        print("2. Listar productos")
        print("3. Buscar un producto")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_producto()
        
        elif opcion == '2':
            listar_productos()
        
        elif opcion == '3':
            nombre_buscar = input("Ingresa el nombre del producto que deseas buscar: ")
            resultado_busqueda = buscar_producto(nombre_buscar)
            print(resultado_busqueda)
        
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    menu()
