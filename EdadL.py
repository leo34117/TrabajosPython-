#!/usr/bin/env python
# coding: utf-8

# In[6]:


ed=int(input("Ingrese una edad "))
com=int(input("""Estas acompañado por un adulto?
                1)Si
                2)No """))
if ed>=18 or com==1:
    print("¡Bienvenido! Disfruta de la película")
else:
    print("Lo siento, no tienes la edad suficiente para ver esta película")


# In[ ]:




