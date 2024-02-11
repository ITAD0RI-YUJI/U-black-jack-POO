import random

def cartaRandom():
    cartaAleatoria = random.choice(range(len(cartasFormadas)))
    cartasFormadas.pop(cartaAleatoria) 
    # carta = print(f"Carta: {cartasFormadas[cartaAleatoria]}")
    return cartasFormadas[cartaAleatoria]

def mostrarMazoUsu():
    for mazo in mazoJugador:
        print(mazo)

def mostrarMazoPc():
    for mazo in mazoCompu:
        print(mazo)

def nombrePC():
    nombreAleatorioPc = random.choice(range(len(nombresPCArray)))    
    return nombresPCArray[nombreAleatorioPc]

nombreUsuario = input("\n• Nombre del usuario: ")
nombresPCArray = ["Itadori" , "Naruto" , "Moa-metal" , "Momo-metal" , "Su-metal"]

valNumerico = [str(i) for i in range(2 , 11)] + ["J", "Q", "K", "AS"]
valSimbolo = ["♣", "♥", "♠", "♦"]

nombrePCPartida = nombrePC() # Eligiendo el nombre del pc

cartasFormadas = [(num , sim) for num in valNumerico for sim in valSimbolo] #Lista por compresnsión (acá formamos todas las tarjetas)

for carta in cartasFormadas:
    numero, simbolo = carta
    print(f"{numero}{simbolo}") # Para que sea "2 ♥" en lugar de "(2, ' ♣')", usar la función f-string en Python. permite formatear cadenas de forma dinámica.

mazoJugador = [] 
mazoCompu = []

for contador in range(4):
    cartaSelec = cartaRandom()
    if(contador < 2):
        mazoJugador.append(cartaSelec)
    else:
        mazoCompu.append(cartaSelec)

    contador += 1

print("\n• Cartas en el mazo de" , nombreUsuario , ": ")
mostrarMazoUsu()

print("\n• El mazo del", nombrePCPartida ,"se podrá ver al final de las partida")

# print("\n• Cartas en el mazo del computador:")
# mostrarMazoPc()
