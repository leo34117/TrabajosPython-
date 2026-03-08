#Cornejo de la Criz Leonardo
 
num = int(input("Ingresa un número entero: "))
# Solicitar al usuario ingresar un número entero


op1= num % 3 == 0
op2= num % 5 == 0
# Evalua si el número es múltiplo de 3 y/o de 5

if op1 and op2: 
    print("es múltiplo de 3 y de 5.")
    #Se imprime si el numero es multiplo de ambos numeros
elif op1:
    print("el numero es múltiplo de 3 pero no de 5.")
    #Se imprime en el caso de que el numero solo sea multiplo de 3
elif op2:
    print("el numero es múltiplo de 5 pero no de 3.")
    #Se imprime en el caso de que el numero solo sea multiplo de 5
else:
    print("no es múltiplo de 3 ni de 5.")
    #Se imprime en el caso de que el numero solo sea multiplo de 3 o 5

