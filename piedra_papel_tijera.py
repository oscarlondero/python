import random

def jugar_piedra_papel_tijera():
    """Simula una partida de Piedra, Papel o Tijera entre dos jugadores."""

    opciones = ["piedra", "papel", "tijera"]
    jugador1 = ""
    jugador2 = ""

    while jugador1 not in opciones:
        jugador1 = input("Jugador 1, elige (piedra, papel o tijera): ").lower()
        if jugador1 not in opciones:
            print("Opción inválida. Intenta de nuevo.")

    while jugador2 not in opciones:
        jugador2 = input("Jugador 2, elige (piedra, papel o tijera): ").lower()
        if jugador2 not in opciones:
            print("Opción inválida. Intenta de nuevo.")


    print("\nResultados:")
    print(f"Jugador 1: {jugador1}")
    print(f"Jugador 2: {jugador2}")

    if jugador1 == jugador2:
        print("¡Empate!")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("¡Jugador 1 gana!")
    else:
        print("¡Jugador 2 gana!")

# Iniciar el juego
jugar_piedra_papel_tijera()