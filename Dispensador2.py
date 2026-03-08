#!/usr/bin/env python
# coding: utf-8


p=15
r=20
g=15
a=10
ga=20

while True:
    op=str(input("""selecciona lo sig
                 117)papas
                 229)refresco
                 343)gomitas
                 464)agua
                 591)galletas
                 0)Apagar el programa
                 """))
    if op=="117":
        print("seleccionanaste papas")
        cobro=int(input("ingrese el dinero "))
        if cobro==p:
            print("toma tu producto")
        elif cobro>p:
            cambio=cobro-p
            print("Tu cambio es",cambio,"Toma tu producto")
        elif cobro<p:
            cambio=p-cobro
            print("Dinero insuficiente")
    elif op==2:
        print("seleccionanaste refresco")
        cobro=int(input("ingrese el dinero "))
        if cobro==r:
            print("toma tu producto")
        elif cobro>r:
            cambio=cobro-r
            print("Tu cambio es",cambio,"Toma tu producto")
        elif cobro<r:
            cambio=r-cobro
            print("Dinero insuficiente")
    elif op==3:
        print("seleccionanaste gomitas")
        cobro=int(input("ingrese el dinero "))
        if cobro==g:
            print("toma tu producto")
        elif cobro>g:
            cambio=cobro-g
            print("Tu cambio es",cambio,"Toma tu producto")
        elif cobro<g:
            cambio=g-cobro
            print("Dinero insuficiente")
    elif op==4:
        print("seleccionanaste cigarros")
        cobro=int(input("ingrese el dinero "))
        if cobro==a:
            print("toma tu producto")
        elif cobro>a:
            cambio=cobro-a
            print("Tu cambio es",cambio,"Toma tu producto")
        elif cobro<a:
            cambio=a-cobro
            print("Dinero insuficiente")
        
    elif op=="0":
            break
  

    else:
        print("Seleccion invalida")

    
print("El progama termino")   
    
