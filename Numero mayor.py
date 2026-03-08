#Cornejo de la Cruz Leonardo
n1=int(input("ingrese un numero ")) #se pide al usurio ingresar un valor
n2=int(input("ingrese un numero ")) 
n3=int(input("ingrese un numero "))
if n1>n2 and n1>n3: #Se evaluan los valores ingresados para saber cual es el mayor
    print("El valor uno es mayor")
elif n2>n1 and n2>n3: 
    print("El valor dos es mayor")
elif n3>n1 and n3>n2:
    print("El valor tres es mayor")
elif n1==n2 and n1>n3 and n2>n3: #Se evaluan los valores ingresados para saber cuales son los mayores
    print("El valor uno y dos son los mayores")
elif n1==n3 and n1>n2 and n3>n2:
    print("El valor uno y tres son los mayores")
else:
    print("todos son iguales") #Se evaluan los valores ingresados en caso de que todos sean iguales 