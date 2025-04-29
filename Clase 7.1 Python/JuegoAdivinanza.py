import random

def generar_numero():
    return random.randint(1, 100)

def adivinar_numero():
    print("¡Bienvenido al juego de adivinanza!")
    print("Debes adivinar el número secreto entre 1 y 100.")
    print("Tienes un máximo de 10 intentos.\n")
    print("¡Buena suerte!")
    
    numero_secreto = generar_numero()
    intentos = 0
    max_intentos = 10

    while intentos < max_intentos:
        adivinanza = input(f"Intento {intentos + 1}: Ingresa tu número: ").strip()
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            if adivinanza < 1 or adivinanza > 100:
                print("El número debe estar entre 1 y 100.")
                continue
        else:
            print("Por favor, ingresa un número válido.")
            continue

        intentos += 1

        if adivinanza == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            return
        elif adivinanza < numero_secreto:
            print("Demasiado bajo.")
        else:
            print("Demasiado alto.")

    print(f"\nLo siento, has agotado tus intentos. El número secreto era {numero_secreto}.")

adivinar_numero()