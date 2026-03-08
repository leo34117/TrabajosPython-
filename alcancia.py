#Cornejo De La Cruz Leonardo 
#Alcancia 
#18/03/2024
n=0
while 1: 
    
    op=input("""Bienvenid@ a tu alcancia, que deseas hacer?
                1)Depositar dinero
                2)Consultar saldo
                3)Retidar dinero
                4)Salir    """)
    
    if op=="1":
        dep=int(input("Bienvenid@ a tu alcancia, deposita tu dinero "))
        n+=dep

    elif op=="2":
        print("Tu saldo es de ", n)

    elif op=="3":
        ret=int(input("Cunato desea retidar? "))
        if ret>n:     
            print("No tienes el saldo sufiente para retidar esa cantidad")
        else:
             n-=ret
             print("Retidaste ", ret, "Ahora tienes ", n)  
             
    elif op=="4":
            break
print("Fin del programa ")
        


        

        
