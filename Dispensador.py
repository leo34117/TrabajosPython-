#!/usr/bin/env python
# coding: utf-8

# In[31]:


cerveza=47
agua=10
coca=20
cafe=25
te=15
codigo=str(input("""Ingresa tu codigo
                    A123
                    B1234
                    C12345 
                    D321
                    E4321 """)).upper()
if codigo=="A123":
    print("Elegiste cerveza, cuesta 47 ")
    cobro=int(input("Ingresa dinero"))
    if cobro==cerveza:
        print("Toma tu cerveza ")
    elif cobro<cerveza:
        cambio=cerveza-cobro
        print("Ingresa mas dinero te falta $" ,cambio)
    elif cobro>cerveza:
        cambio=cobro-cerveza
        print("Toma tu cambio" ,cambio)
if codigo=="B1234":
    print("Elegiste agua, cuesta 10 ")
    cobro=int(input("Ingresa dinero "))
    if cobro==agua:
        print("Toma tu agua ")
    elif cobro<agua:
        cambio=agua-cobro
        print("Ingresa mas dinero te falta $" ,cambio)
    elif cobro>agua:
        cambio=cobro-agua
        print("Toma tu cambio" ,cambio)
if codigo=="C12345":
    print("Elegiste COCA, cuesta 20 ")
    cobro=int(input("Ingresa dinero "))
    if cobro==coca:
        print("Toma tu cocacola ")
    elif cobro<coca:
        cambio=coca-cobro
        print("Ingresa mas dinero te falta $",cambio)
    elif cobro>coca:
        cambio=cobro-coca
        print("Toma tu cambio" ,cambio)
if codigo=="D321":
    print("Elegiste Cafe, cuesta 25 ")
    cobro=int(input("Ingresa dinero "))
    if cobro==cafe:
        print("Toma tu Cafe ")
    elif cobro<cafe:
        cambio=cafe-cobro
        print("Ingresa mas dinero te falta $",cambio)
    elif cobro>cafe:
        cambio=cobro-cafe
        print("Toma tu cambio" ,cambio)
if codigo=="E4321":
    print("Elegiste Té, cuesta 15 ")
    cobro=int(input("Ingresa dinero "))
    if cobro==te:
        print("Toma tu Té ")
    elif cobro<te:
        cambio=te-cobro
        print("Ingresa mas dinero te falta $",cambio)
    elif cobro>te:
        cambio=cobro-te
        print("Toma tu cambio" ,cambio)
        
else:
    print("Codigo invalido como tu .i.")
    
       


# In[ ]:




