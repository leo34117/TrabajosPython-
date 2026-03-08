#!/usr/bin/env python
# coding: utf-8

# # operadores de asignacion
# 

# In[1]:


#Asignacion de suma(+=)
c=9
c+=3
print(c)


# In[3]:


x=13
x-=9 # el valor que estaba en x no se sustituye si no se resta 
print(x)


# In[4]:


x=13
x*=9 
print(x)


# In[5]:


x=13
x/=9 
print(x)


# In[6]:


x=13
x//=9 
print(x)


# In[8]:


#Asignacion de exponente
x=5
x**=2 
print(x)


# In[9]:


#asignacion de modulo, residuo de la divicion
x=10
x%=2
print(x)


# In[28]:


print("!piedra papel o tijera¡")
ju1=str(input("""Que eliges
                piedra
                papel
                tijera """))
pc=str(input("""Que eliges
                 piedra
                 papel
                 tijera """))

if ju1=="piedra" and pc=="tijera":
    print("gana piedra")
elif ju1=="papel" and pc=="tijera":
    print("gana tijera")
elif ju1=="papel" and pc=="piedra":
     print("gana papel")
elif ju1=="tijera" and pc=="piedra":
    print("gana piedra")
elif ju1=="piedra" and pc=="papel":
    print("gana papel")
elif ju1=="tijera" and pc=="papel":
    print("gana tijera")
elif ju1=="papel" and pc=="papel":
    print("empate")
elif ju1=="tijera" and pc=="tijera":
    print("empate")
elif ju1=="piedra" and pc=="piedra":
    print("empate")
else:
    print("no vale")

   


# In[ ]:




