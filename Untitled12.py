#!/usr/bin/env python
# coding: utf-8

# In[2]:


edad=int(input("ingresa tu edad"))
if edad>=18:
    print("es mayor de edad") #identacion
else:
    print("Eres menor de edad")


# In[35]:


año=int(input("ingresa un año "))
a=año%4
if a==0:
    print("es año bisiesto ") #identacion
else: 
    print("no es año bisiesto ")


# In[42]:


num=int(input("ingresa un numero "))
n=num%2
if n==0:
    print("es par ") #identacion
else: 
    print("es impar ")


# In[48]:


num=int(input("ingresa un numero "))
if num>=0:
    print("es positivo ") #identacion  
else: 
    print("es negativo ")


# In[63]:


edad=int(input("""ingresa tu edad; 
1) ingrese entre el 0 1 2 para un bebe
2) ingrese entre 3 4 y menos de 18 para menor de edad """))

if edad>=65:
    print("es de un anciano ") #identacion   
    
elif edad<2:
    print("es un bebe ")
elif edad>=18:
    print("Es mayor de edad ")
else:
    print("Eres menor de edad ")


# In[70]:


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
    elif num2==0:
        divicion=num1/num2
        divicion=str(divicion)
    print("El resultado es " +divicion)
else:
    print("No existe ")


# In[ ]:




