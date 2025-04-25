def simular_combate():
    while True:
        try:
            ataque_jugador = int(input("Ingresa el poder de ataque del jugador: "))
            if ataque_jugador >= 0:
                break
            else:
                print("El poder de ataque no puede ser negativo. Inténtalo de nuevo.")
        except ValueError:
            print("Eso no parece un número entero. Inténtalo de nuevo.")

    while True:
        try:
            defensa_enemigo = int(input("Ingresa el poder de defensa del enemigo: "))
            if defensa_enemigo >= 0:
                break
            else:
                print("El poder de defensa no puede ser negativo. Inténtalo de nuevo.")
        except ValueError:
            print("Eso no parece un número entero. Inténtalo de nuevo.")

    if ataque_jugador > defensa_enemigo:
        print("¡El jugador ha ganado el combate!")
    elif ataque_jugador == defensa_enemigo:
        print("¡El combate ha terminado en empate!")
    else:
        print("¡El jugador ha perdido el combate!")

if __name__ == "__main__":
    simular_combate()
