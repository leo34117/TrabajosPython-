# Diccionario con categorías de productos y sus respectivas opciones
productos = {
    "comida": {
        "1": {"nombre": "pollo", "precio": 50},
        "2": {"nombre": "pizza", "precio": 80},
        "3": {"nombre": "hamburguesa", "precio": 60}
    },
    "bebidas": {
        "1": {"nombre": "agua", "precio": 15},
        "2": {"nombre": "refresco", "precio": 20},
        "3": {"nombre": "jugo", "precio": 18}
    },
}

# Lista para almacenar productos seleccionados
carrito = []

while True:
    # Mostrar el menú principal
    print("""
               BIENVENIDO A MAQUINA EXPENDEDORA
               Ingresa el código para elegir producto:
                            1 - Agregar producto
                            2 - Sacar ticket de compras
                            0 - Para salir         
    """)

    codigo = input("Ingresa tu opción: ")

    if codigo == "1":
        # Mostrar categorías disponibles
        print("\nCategorías disponibles:")
        for categoria in productos:
            print(categoria.capitalize())  # Mostrar las categorías de productos
        
        categoria_elegida = input("Ingresa la categoría (comida/bebidas): ").lower()

        if categoria_elegida in productos:
            print("\nProductos en la categoría " + categoria_elegida + ":")
            for key, value in productos[categoria_elegida].items():
                print(f"{key}. {value['nombre']} - ${value['precio']}")

            producto_codigo = input("Ingresa el código del producto que deseas agregar: ")
            if producto_codigo in productos[categoria_elegida]:
                carrito.append(productos[categoria_elegida][producto_codigo])
                print(f"Has agregado {productos[categoria_elegida][producto_codigo]['nombre']} al carrito.\n")
            else:
                print("Código de producto inválido.\n")
        else:
            print("Categoría inválida.\n")

    elif codigo == "2":
        # Mostrar ticket de compras
        if len(carrito) > 0:
            print("\nTicket de compras:")
            total = 0
            for item in carrito:
                print(f"{item['nombre']} - ${item['precio']}")
                total += item['precio']
            print(f"\nTotal a pagar: ${total}\n")
        else:
            print("\nEl carrito está vacío.\n")

    elif codigo == "0":
        print("Gracias por usar la máquina expendedora. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.\n")