#Leonardo Cornejo De La Cruz

correo = input("Ingresa tu dirección de correo electrónico: ")
print(correo.find("@"))
print(correo.find("."))
if correo.find("@") != -1 and correo.find(".") != -1:
    print("La dirección de correo electrónico es válida")
else:
    print("La dirección de correo electrónico no es válida.")

contra= input("Ingresa la contraseña: ")
print(contra.find("*"))
print(contra.find("5"))
if contra.find("*") != -1 and contra.find("5") != -1:
    print("Contraseña correcta, inciando seccion")
elif contra.find("*") != -1 or contra.find("5") != -1:
    print("Contraseña correcta, inciando seccion")
else:
    print("contraseña incorrecta")