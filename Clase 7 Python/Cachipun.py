def Piedra_Papel_Tijera():
    import random
    opciones = ["piedra", "papel", "tijera"]
    usuario_ganador = 0
    computadora_ganador = 0

    print("Bienvenido a Piedra, Papel o Tijera (Mejor de 3)")

    while usuario_ganador < 2 and computadora_ganador < 2:
        print("\nElige una opción:")
        print("1. piedra")
        print("2. papel")
        print("3. tijera")
        eleccion = input("Ingresa 1, 2 o 3: ").strip()

        if eleccion == "1":
            usuario = "piedra"
        elif eleccion == "2":
            usuario = "papel"
        elif eleccion == "3":
            usuario = "tijera"
        else:
            print("Opción no válida.")
            continue

        computadora = random.choice(opciones)
        print(f"Tú elegiste: {usuario}")
        print(f"La computadora eligió: {computadora}")

        if usuario == computadora:
            print("Empate.")
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            print("¡Ganaste esta ronda!")
            usuario_ganador += 1
        else:
            print("La computadora gana esta ronda.")
            computadora_ganador += 1

        print(f"Marcador: Tú {usuario_ganador} - Computadora {computadora_ganador}")

    if usuario_ganador == 2:
        print("\n¡Felicidades! Ganaste el juego.")
    else:
        print("\nLa computadora ganó el juego.")

Piedra_Papel_Tijera()