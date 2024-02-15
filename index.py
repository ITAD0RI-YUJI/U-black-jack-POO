import random 

# funciones del proyecto 
def nombrePcFunction():
    nombrePcAleatorio = random.choice(range(len(nombrePcArray)))
    return nombrePcArray[nombrePcAleatorio]

def repartirCartas(mazo):
    for i in range(2):
        indiceAleatorio = random.choice(range(len(cartasJuego)))
        cartasJuego.pop(indiceAleatorio)
        mazo.append(cartasJuego[indiceAleatorio])
        
    i += 1

def agregarCartaFunction(mazo):
    for i in range(1):
        indiceAleatorio = random.choice(range(len(cartasJuego)))
        cartasJuego.pop(indiceAleatorio)
        mazo.append(cartasJuego[indiceAleatorio])
        
    i += 1

def sumaMazo(mazo):
    puntos = 0

    for carta in mazo:
        num , _ = carta

        if num.isdigit():
            puntos += int(num)
        elif num == "J" or num == "Q" or num == "K":
            puntos += 10
        else:
            if puntos > 10 and num == "A":
                puntos += 1
            else:
                puntos += 11
    
    return puntos

def mostrarMazo(mazo):
    for i in mazo:
        print(i)

def compararFunction(sumaUsu , sumaPc):
    if sumaPc > sumaUsu and sumaPc <= 21:
        print("\n• El ganador es ", nombrePcPartida)
    
    elif sumaUsu > sumaPc and sumaUsu <= 21:
        print("\n• El ganador es ", nombreUsuario)

    else:
        print("\n• No hay Ganador")
    

valNumericos = [str(i) for i in range(2 , 11)] + ["J", "Q", "K", "A"]
valSimbolos = ["♣", "♥", "♠", "♦"]
cartasJuego = [(num , simb) for num in valNumericos for simb in valSimbolos]

mazoJugador = []
mazoComputador = []

nombrePcArray = ["Moa-metal" , "Momo-metal" , "Su-metal"]

nombreUsuario = input("Ingresa tu nombre de usuario: ")
nombrePcPartida = nombrePcFunction()

print("\nJugadores: \n","•",nombreUsuario, "\n" ,"•",nombrePcPartida)

repartirCartas(mazoJugador)
repartirCartas(mazoComputador)

turno = 0
pcPlantada = False
usuarioPlantado = False
sumaMazoPc = 0
sumaUsuario = 0

while True:
    if turno == 0:
        while True:
            print("\nEl mazo de", nombreUsuario, "está compuesto por:")
            mostrarMazo(mazoJugador)
            sumaUsuario = sumaMazo(mazoJugador)
            print("La suma del mazo es: ", sumaUsuario)

            agregarCarta = input("\n¿Quieres agregar una carta a tu mazo? ")
            if agregarCarta == "no" or agregarCarta == "NO":
                usuarioPlantado = True
                break
            if agregarCarta != "no":
                agregarCartaFunction(mazoJugador)
                break
    else:
        print("\nEl mazo de", nombrePcPartida, "está compuesto por:")
        mostrarMazo(mazoComputador)

        sumaMazoPc = sumaMazo(mazoComputador)
        if sumaMazoPc <= 16:
            agregarCartaFunction(mazoComputador)
            print("La suma del mazo es: ", sumaMazoPc)
        else:
            pcPlantada = True
            print("La suma del mazo es: ", sumaMazoPc)
    
    if pcPlantada == True and usuarioPlantado == True:
        compararFunction(sumaUsuario , sumaMazoPc)

    turno = (turno + 1) % 2