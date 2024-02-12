import random

def cartaRandom():
    cartaAleatoria = random.choice(range(len(cartasFormadas)))
    cartasFormadas.pop(cartaAleatoria) 
    return cartasFormadas[cartaAleatoria]

def mostrarMazo(dueño):
    for mazo in dueño:
        print(mazo)

def sumarNumerosMazo(mazo):
    suma = 0
    for carta in mazo:
        numero, _ = carta  # Desempaqueta solo el número, el símbolo no es necesario

        if numero.isdigit():  # Comprueba si el número es un dígito
            suma += int(numero)  # Suma solo si es un dígito
        elif numero == "J" or numero == "Q" or numero == "K":
            suma += 10
        elif numero == "AS":
            valorAS = int(input("• Tienes un 'AS' cuánto quieres que valga? 11 o 1?: "))
            suma += valorAS

    return suma

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
mostrarMazo(mazoJugador)
print("\n• La suma de tu mazo es: ", sumarNumerosMazo(mazoJugador))

print("\n• El mazo del", nombrePCPartida ,"se podrá ver al final de las partida")

print("\n• Cartas en el mazo de ", nombrePCPartida, ":")
mostrarMazo(mazoCompu)
