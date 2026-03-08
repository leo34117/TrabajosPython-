#Cornejo de la Cruz Leonardo
#Universidad Politecnica de Texcoco 
#13/11/2024

# llamado de las bibliotecas nesesarias 
# para le funcionamiento de la interfaz 
import tkinter as tk
from tkinter import messagebox

# Funciones donde se almacena las operaciones 
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multi(a, b): 
    return a * b

def division(a, b):

    if b == 0:
        return "No se puede dividir entre 0"
    else:
        return a / b

def potencia(a, b):
     
    return a ** b
    
def raiz(a, b):
    
    resulta = a** 0.5
    resultb = b ** 0.5  
    return resulta, resultb  

def porcen(a, b):
    
    return a * b / 100

def area(a, b):
    

    resulta = a ** 2 * 3.1516  
    resultb = b ** 2 * 3.1516
    return resulta, resultb 

# Diccionario donde se almacenan las operaciones con su codigo 
operaciones = {"1": suma,
               "2": resta,
               "3": multi,
               "4": division,
               "5": potencia,
               "6": raiz,
               "7": porcen,
               "8": area,}


# Función para la introduucion de los datos y resultados 
def calcular(operacion):
    a_text = entry_a.get()
    b_text = entry_b.get()

    # Verificación básica de que los inputs son números
    if not a_text.isdigit() or not b_text.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        return

    # Conversión a float
    a = float(a_text)
    b = float(b_text)

    # Realiza la operación y muestra el resultado
    if operacion in operaciones:
        resultado = operaciones[operacion](a, b)
        # Si es una operación con dos resultados
        if isinstance(resultado, tuple):  
            result_text = f"Resultado A: {resultado[0]}, Resultado B: {resultado[1]}"
        else:
            result_text = f"Resultado: {resultado}"
        messagebox.showinfo("Resultado", result_text)
    else:
        messagebox.showerror("Operación no válida.")

# Interfaz gráfica con tkinter
root = tk.Tk()
root.title("Calculadora ")
root.geometry("200x400")

# Entradas para los números
tk.Label(root, text="Ingresa el primer número (A):").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Ingresa el segundo número (B):").pack()
entry_b = tk.Entry(root)
entry_b.pack()

# Botones para cada operación
for text, code in [("Suma", "1"), ("Resta", "2"), ("Multiplicación", "3"),
                   ("División", "4"), ("Potencia", "5"), ("Raíz", "6"),
                   ("Porcentaje", "7"), ("Área", "8")]:
    tk.Button(root, text=text, command=lambda op=code: calcular(op)).pack(fill="x", padx=10, pady=2)

# Ejecuta la interfaz gráfica en bucle 
# para no tener que correr el programa varias veces 
root.mainloop()
 