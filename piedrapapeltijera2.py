print("!piedra papel o tijera¡")
import random 
while 1:
    modo=str(input("""Que modo de juego escoges?
            1) 1Vs1
            2) 1VsPC 
            0) Salir del juego
                """))
    if modo=="1":
        ju1=str(input("""Que eliges
                        1)piedra
                        2)papel
                        3)tijera """))
        ju2=str(input("""Que eliges
                        1)piedra
                        2)papel
                        3)tijera """))
        if ju1=="1" and ju2=="3":
            print("gana piedra")
        elif ju1=="2" and ju2=="3":
            print("gana tijera")
        elif ju1=="2" and ju2=="1":
            print("gana papel")
        elif ju1=="3" and ju2=="1":
            print("gana piedra")
        elif ju1=="1" and ju2=="2":
            print("gana papel")
        elif ju1=="3" and ju2=="2":
            print("gana tijera")
        elif ju1=="2" and ju2=="2":
            print("empate")
        elif ju1=="3" and ju2=="3":
            print("empate")
        elif ju1=="1" and ju2=="1":
            print("empate")

        else:
            print("no vale")
    elif modo=="0":
        break 
    if modo=="2":
        ju1=str(input("""Que eliges
                        1)piedra
                        2)papel
                        3)tijera """))
        op=("1","3")
        pc=random.choice(op)
        print("PC", pc)
        if ju1=="1" and pc=="3":
                print("gana piedra")
        elif ju1=="2" and pc=="3":
            print("gana tijera")
        elif ju1=="2" and pc=="1":
            print("gana papel")
        elif ju1=="3" and pc=="1":
            print("gana piedra")
        elif ju1=="1" and pc=="2":
            print("gana papel")
        elif ju1=="3" and pc=="2":
            print("gana tijera")
        elif ju1=="2" and pc=="2":
            print("empate")
        elif ju1=="3" and pc=="3":
            print("empate")
        elif ju1=="1" and pc=="1":
            print("empate")    
        else:
            print("no vale")
            