import random

def juego():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("¡Bienvenido al juego de adivinación de números!")
    print("Estoy pensando en un número entre 1 y 10.")

    while True:
        intento = int(input("Por favor, introduce un número: "))
        intentos += 1

        if intento < numero_secreto:
            print("¡Demasiado bajo!")
        elif intento > numero_secreto:
            print("¡Demasiado alto!")
        else:
            print(f"¡Has acertado después de {intentos} intentos!")
            break

juego()
