#!/usr/bin/env python
# coding: utf-8

# In[22]:


eur=0.85
mxn=20.15
yen=109.42
us=float(input("Ingresa la cantidad de dolares que quieres convertir "))
conver=input("""Elige una moneda
                1)eur
                2)mxn
                3)yen """)
if conver=="1":
    res=eur*us
    res="{:.2f}".format(res)
    print(res)
elif conver=="2":
    res=mxn*us
    res="{:.2f}".format(res)
    print(res)
elif conver=="3":
    res=yen*us
    res="{:.2f}".format(res)
    print(res)
else:
    print("Eleccion no valida")


# In[ ]:




