#Cornejo de la Cruz Leonardo
#Caja Registradora
#20/03/2024

p=10
a=5
r=10
pan=5
total=0
while True:
    op=input("""Ingrese el codigo del producto 
             a1
             b2
             c3
             d4
             1)total y pago
             """)
    if op=="a1":
        total+=p
    elif op=="b2":
        total+=a
    elif op=="c3":
        total+=r
    elif op=="d4":
        total+=pan
    elif op=="1":
        print("El total es", total)
        me=input("""Escoja un metodo de pago
             1)Tarjeta
             2)Efectivo """)
        if me=="1":
            print("Pase la tarjeta por la terminal y tome sus productos")
        elif me=="2":
            mx=0
            mx=int(input("Ingrese el efectivo "))
            if mx>=total:
                print("Tome sus productos")
            elif mx<total:
                print("Saldo insuficiente, intente de nuevo")
        else:
            print("Opcion invalida")
    else:
        print("Opcion invalida")
        break 
            

        