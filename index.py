import random

valNumerico = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "AS"]
valSimbolo = [" ♣", " ♥", " ♠", " ♦"]

def cartaRandom():
    cartaAleatoria = random.choice(range(len(cartasFormadas))) 
    carta = print(f"Carta: {cartasFormadas[cartaAleatoria]}")
    return carta

cartasFormadas = [(num , sim) for num in valNumerico for sim in valSimbolo] #Lista por compresnsión (acá formamos todas las tarjetas)

for carta in cartasFormadas:
    numero, simbolo = carta
    #print(f"{numero}{simbolo}") # Para que sea "2 ♥" en lugar de "(2, ' ♣')", usar la función f-string en Python. permite formatear cadenas de forma dinámica.


mazoJugador = [] #colocar función para que escoja número random (posiciones) de las cartas ya formadas
mazoCompu = []

carta = cartaRandom()
carta = cartaRandom()
