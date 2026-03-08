# Cornejo de la Cruz Leonardo
# 21/09/2024

import math
import matplotlib.pyplot as plt
import numpy as np

while True:
    
    a = float(input("ingrese un numero: "))
     
    if a==0:
        print("No es una raiz cuadrada")
        break

    b = float(input("ingrese un numero: "))
    c = float(input("ingrese un numero: "))
    if b**2-4*a*c<0:
        print("No tiene soluciones reales")
    else:
        
        r1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        print(r1)
        r2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        print(r2)
plt.plot(r1,r2)
plt.show()