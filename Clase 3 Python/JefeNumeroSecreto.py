import random

def generar_numero_secreto():
    return random.randint(1, 5)

def jugar_numero_secreto():
    numero_secreto = generar_numero_secreto()
    intentos = 3

    print("¡Enfrentas al jefe final!")
    print("El jefe tiene un número secreto entre 1 y 5.")
    print("Tienes 3 intentos para adivinarlo.")

    while intentos > 0:
        intento = int(input(f"Te quedan {intentos} intentos. Ingresa tu número: "))
        
        if intento == numero_secreto:
            print("¡Adivinaste el número secreto! ¡Ganaste la batalla!")
            return
        else:
            print("Número incorrecto.")
        
        intentos -= 1

    print("Has fallado los 3 intentos. El jefe te ha derrotado.")

# Llamar a la función principal
jugar_numero_secreto()