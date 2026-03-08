#Cornejo De La Cruz Leonardo

print("!ESCONDIDAS¡") 
#Se imprime el nombre del juego
ju1=str(input("ingresa el nombre del jugador que ves? ")) 
#Se pide al usuario ingresar en nombre del jugador al que ve
posicion=str(input( "A donde ves al jugador? ")) 
#Se pregunta al usuario la pocicion del jugador
dis=int(input("A que distancia ves al jugador? ")) 
#Se pregunta al usuario la distancia a la ve al jugador
if dis==0 or dis==1 or dis==2 or dis==3 or dis==4 or dis==5: 
#Se evalua la distancia en base a que numero es igual del 0 al 5
    print("¡UNO, DOS, TRES, POR " ,ju1  +"¡QUE ESTÁ " ,posicion ) 
#Si la distnacia ingresada por el usuario es igual a cualquier numero del 0 al 5 se imprime este mensaje
else:
    print("FALSA ALARMA. SIGUE BUSCANDO") #Si no, se imprime este mensaje