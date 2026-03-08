#CALCULADORA BASICA, 19/01/2024
#LEONARDO CORNEJO DE LA CRUZ

num1=float(input("ingresa un numero "))
num2=float(input("ingresa un numero "))
op=int(input("""ingresa una opcion; 
1) suma
2) resta
3) multiplicacion
4) divicion 
"""))
if op==1:
    suma=num1+num2
    suma=str(suma)
    print("El resultado es " +suma) 
    
elif op==2:
    resta=num1-num2
    resta=str(resta)
    print("El resultado es " +resta)
    
elif op==3:
    multiplicacion=num1*num2
    multiplicacion=str(multiplicacion)
    print("El resultado es " +multiplicacion)
    
elif op==4:
    if num2==0:
        print("no se puede dividir entre 0")
    elif num2>0:
        divicion=num1/num2
        divicion=str(divicion)
    print("El resultado es " +divicion)
else:
    print("No existe ")