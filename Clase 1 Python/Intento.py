import random
numero_secreto = random.randint(1, 5)
intentos_maximos = 3

print("¡Adivina el número secreto del jefe (entre 1 y 5)!")
print(f"Tienes {intentos_maximos} intentos.")


for intento_actual in range(intentos_maximos):

    try:
        adivinanza_str = input(f"Intento #{intento_actual + 1}: Ingresa tu número: ")
        adivinanza_num = int(adivinanza_str) 


        if adivinanza_num == numero_secreto:
            print(f"\n¡Correcto! El número secreto era {numero_secreto}. ¡Has ganado!")
            break 
        else:

            print("Incorrecto...")

            intentos_restantes = intentos_maximos - (intento_actual + 1)
            if intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intentos.")

    except ValueError:

        print("Eso no es un número válido. Intenta de nuevo.")

        intentos_restantes = intentos_maximos - (intento_actual + 1)
        if intentos_restantes > 0:
             print(f"Te quedan {intentos_restantes} intentos.")

else:
    print(f"\n¡Se acabaron los intentos! El número secreto era {numero_secreto}. Has perdido.")

