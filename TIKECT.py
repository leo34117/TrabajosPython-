# 1.- Cornejo De La Cruz Leonardo	           231650171
# 2.- Barajas Gómez Diego Leonel 	           221550204
# 3.- Buenaventura Soriano Francisco Javier	   231650041
# 4.- Lugo Sánchez Rodrigo	                   231650201
# 5.- Espinoza Hernández David Alejandro 	   231650321

# Variables y listas a usar durante el programa 
total = 0
compra = []
# Diccionario con los datos de los productos 
productos = {
    "1": {"nombre": "Atun","precio":30,"categoria": "Comida"},
    "2": {"nombre": "Frijoles","precio":26,"categoria": "Comida"},
    "3": {"nombre": "Tortillas","precio":20,"categoria": "Comida"},

    "4": {"nombre": "Agua", "precio": 15,"categoria": "Bebidas"},
    "5": {"nombre": "Refresco", "precio": 20,"categoria": "Bebidas"},
    "6": {"nombre": "Cerveza", "precio": 40,"categoria": "Bebidas"},

    "7": {"nombre": "Carlos V","precio":10,"categoria": "Dulces"},
    "8": {"nombre": "Chips", "precio": 15,"categoria": "Dulces"},
    "9": {"nombre": "Tupsi", "precio": 5,"categoria": "Dulces"},
}

# Bucle para ingresar lo productos y pedri el Ticket
while True:
    op = input("""
                                    ░░░░░░▄█▀█▄░░░░░░░░░░░░░░░
                                    ░▄█▀▀▀▀░░░░▀█▄▄▄▄▄▄▄░░░░░░
                                    █▀░░░░░░░░░░░░░░░░░▀█░░░░░
                                    ▀▄░▄░░░░░░░░░░░░░░░▄█░░░░░
                                    ░█████▄▄▄▄▄██▄▄▄█▀▀█░░░░░░
                                    ░█▀█░░░░▀░░░░░▀░░░░█▀▀▀▀▀█
                                    ░█░███▄▄▄▄░░░▄▄▄▄▄██▀▀██░█
                                    ░█░███░████▀████░███░░█░░█
                                    ░█▄███░████░████░███░░█░█▀
                                    ░░░███░████░████░███▄▄█░█░
                                    ░░░███░████░████░███░░░▄█░
                                    ░░░███░████░████░███▀▀▀▀░░
                                    ░░▄███▄████░████▄███▄░░░░░
                                    ░░███▀███████████▀███░░░░░
                                  INGRESE EL CODIGO DEL PRODUCTO 
                                          QUE DESEA :).
                          Categorías:
                              Comida:           
                                       1) Atun
                                       2) Frijoles
                                       3) Tortillas
                                      
                              Bebidas:
                                       4) Agua
                                       5) Refresco
                                       6) Cerveza 
                                 
                               Dulces: 
                                       7) Carlos V
                                       8) Chips
                                       9) Paleta Tupsi


                          0) Ticket 
""")

    # Lista de posibilades para ejecutar las diferentes funciones 
    if op == "0": # Pedir ticket de compra
         # Impresion del ticket del compra 
         print("\n--------- TICKET DE COMPRA ---------")
         # Ordena los productos por categorias e imprime el resultado 
         for categoria, items in categorias.items():
            print(f"\nCategoría: {categoria}")
            for item in items:
                print(f"{item['producto']} - Cantidad: {item['cantidad']} - Precio: {item['precio_unitario']} - Subtotal: {item['subtotal']}")
            print(f"Total en {categoria}: {totales_categorias[categoria]}")
         print(f"\nTotal general: {total_general}\n")
         # Operacion para sacar los porcentajes y impresion del resultado 
         for categoria, total in totales_categorias.items():
             porcentaje = (total / total_general) * 100
             print(f"Porcentaje del total gastado en {categoria}: {porcentaje:.2f}%")
         # Operacion para saber cule fuel la categoria en la que se gasto mas 
         categoria_max = max(totales_categorias, key=totales_categorias.get)
         print(f"\nLa categoría con mayor gasto fue: {categoria_max} con {totales_categorias[categoria_max]}")
         break # Fin del bucle while 
    # Evaluar si el producto se encuentrea en el diccionario      
    elif op in productos:
        producto = productos[op]
        cantidad = int(input(f"Ingrese la cantidad de {productos[op]['nombre']}: "))
        # Agregar porducto a la lista de compra 
        compra.append({"producto": productos[op]["nombre"], 
                           "categoria": productos[op]["categoria"], 
                           "precio": productos[op]["precio"], 
                           "cantidad": cantidad})   
    # Mensaje en caso de que el producto no este en la lista
    else: 
        print("Producto no válido, intente nuevamente.")
    # Asigna el producto a una categoria 
    categorias = {}
    for item in compra:
        # Operacion para saber el precio total de los productos individuales 
        categoria = item["categoria"]
        subtotal = item["precio"] * item["cantidad"]
        # Evaluar si el producto esta en categorias 
        if categoria not in categorias:
            categorias[categoria] = []
        # Agrega el producto a una nueva lista con elnombre de la categoria 
        categorias[categoria].append({"producto": item["producto"], 
                                      "precio_unitario": item["precio"], 
                                      "cantidad": item["cantidad"], 
                                      "subtotal": subtotal})
    # Operacion para saber el saldo total
    totales_categorias = {}
    total_general = 0
    # Guardaro de los resultados en sus respectivas variables para su imprecion 
    for categoria, items in categorias.items():
        total_categoria = sum(item["subtotal"] for item in items)
        totales_categorias[categoria] = total_categoria
        total_general += total_categoria
   


