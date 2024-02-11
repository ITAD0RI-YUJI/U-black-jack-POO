import random

valNumerico = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "AS"]
valSimbolo = [" ♣", " ♥", " ♠", " ♦"]

def cartaRandom():
    cartaAleatoria = random.choice(range(len(cartasFormadas)))
    cartasFormadas.pop(cartaAleatoria) 
    # carta = print(f"Carta: {cartasFormadas[cartaAleatoria]}")
    return cartasFormadas[cartaAleatoria]

def mostrarMazo():
    for mazo in mazoJugador:
        print(mazo)

cartasFormadas = [(num , sim) for num in valNumerico for sim in valSimbolo] #Lista por compresnsión (acá formamos todas las tarjetas)

for carta in cartasFormadas:
    numero, simbolo = carta
    #print(f"{numero}{simbolo}") # Para que sea "2 ♥" en lugar de "(2, ' ♣')", usar la función f-string en Python. permite formatear cadenas de forma dinámica.


mazoJugador = [] 
mazoCompu = []

for contador in range(4):
    cartaSelec = cartaRandom()
    if(contador < 2):
        mazoJugador.append(cartaSelec)
    else:
        mazoCompu.append(cartaSelec)

    contador += 1

print("• Cartas en el mazo del usuario:")

mostrarMazo()
