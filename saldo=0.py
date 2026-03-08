saldo=0
deposito=0
retiro=0

while True:
    opcion=int(input("""ingresa la opción a realizar
                            1 para depositar dinero
                            2 para retirar dinero
                            3 para consultar Saldo
                            4 Para cerrar sesion
                            """))
     
    if opcion==1:
        dinero=5
        deposito=int(input("Ingresa la cantidad a depositar "))
        saldo=saldo+deposito
        print(" Se depositó: ",deposito) 

    elif opcion==2:
        retiro=int(input("Ingrese la cantidad a retirar"))
        saldo=saldo-retiro
        print("Se ha retirado: ",retiro)
        
    elif opcion==3:       
        print("Su saldo actual es: ", saldo) 
        
    elif opcion==4:
        break
print("ha cerrado sesión")