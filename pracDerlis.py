# Cornejo de la Cruz Leonardo 
# 17/09/2024
numr = int(input("Introdusca el numero de registroa a ingresar "))
print("El numero de registroa a ingresar es:", numr)

lista = []
edtotal = 0

for i in range(0, numr): 
    datos = input("Escribe nombre y edad (Nombre, Edad): " ) 
    nom, ed = datos.split(",")
    ed = int and float(ed)
    lista.append((str(nom), ed))
    edtotal += ed
media = edtotal / numr
print("La media de las edades es de:", media, "años")

mayores = [lista for lista in lista if lista[1] > media]

mayedad = [lista for lista in lista if lista[1] >= 18]

menedad = [lista for lista in lista if lista[1] < 18]

print("Personas con edad mayor al promedio:")
for lista in mayores:
    print(f"Nombre: {lista[0]}, Edad: {lista[1]}")

print("Personas mayores de edad:")
for lista in mayedad:
    print(f"Nombre: {lista[0]}, Edad: {lista[1]}")

print("Personas menores de edad:")
for lista in menedad:
    print(f"Nombre: {lista[0]}, Edad: {lista[1]}")