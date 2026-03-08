#MAQUINA DISPENASADORA 

from datetime import datetime

total = 0

productos = {
    "117": {"nombre":"Papas","precio":20,"cantidad":20,"caducidad":datetime(2025,4,1)},
    "229": {"nombre":"Gomitas","precio":15,"cantidad":15,"caducidad":datetime(2025,6,20)},
    "343": {"nombre":"Agua","precio":10,"cantidad":22,"caducidad":datetime(2026,8,22)},
    "464": {"nombre":"Refresco","precio":20,"cantidad":10,"caducidad":datetime(2026,11,10)},
    "591": {"nombre":"Galletas","precio":15,"cantidad":13,"caducidad":datetime(2025,10,20)}
}

while 1:
    op=str(input("""

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
                                                
                                        117) Papas
                                        229) Gomitas
                                        343) Agua
                                        464) Refresco
                                        591) alletas
                                        0) Salir 
"""))
    
    if op=="0":
        print("Gracias por su visita!; Total:",total)
        break

    elif op in productos:
        producto = productos[op]
        if producto ["cantidad"] > 0:
            if datetime.now() <= producto["caducidad"]:
                print(f"Usted ha selecionado {producto['nombre']}. Por favor, pague: {producto['precio']}")
                cobro=int(input("Ingrese su pago"))
                if cobro==producto["precio"]:
                    print("Gracias por su compra")
                    total+=producto["precio"]
                    producto["caducidad"]-=1
                    print(f"Quedan {producto['cantidad']} productos de {producto['nombre']} en el inventario.")
                elif cobro<producto["precio"]:
                    faltante=producto["precio"]-cobro
                    print("Le falta $",faltante)
                    cobro_extra=int(input("Ingrse el monto faltante para resivir su producto"))
                    cobro+=cobro_extra
                    if cobro>=producto["precio"]:
                        print("Gracias, tome su producto")
                        cambio=cobro-producto["precio"]
                        producto["caducidad"]-=1
                        print("Su cambio es $", cambio)
                        print(f"Quedan {producto['cantidad']} productos de {producto['nombre']} en el inventario.")
                    else:
                        print("El cobro sigue sineod insuficiente ")
                elif cobro>producto["precio"]:
                    cambio=cobro-producto["precio"]
                    print("Gracias por su compra su cambio es {}".format(cambio))
                    producto["cantidad"]-=1
                    print(f"Quedan {producto['cantidad']} productos de {producto['nombre']} en el inventario.")
            else:
                print("El producto no se puede vender por que esta caducado.\n Elige otro producto")
        else:
            print("El producto no se puede vender por que esta agotado.\n Elige otro producto")