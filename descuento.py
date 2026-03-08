#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[24]:


com=int(input("Ingrese el monto total de la compra "))

if com>=100 and com<200:
    des=com/100*10
    res=com-des
    print("Tiene un descuento del 10%",res)
elif com>=200 and com<500:
    des=com/200*20
    res=com-des
    print("Tiene un descuento del 20%",res)
elif com>=500:
    des=com/500*30
    res=com-des
    print("Tiene un descuento del 30%",res)
elif com<100:
    print("No se aplica ningun descuento")
    


# In[ ]:




