def elegir_dificultad():
    while True:
        print("\nElige la dificultad:")
        print("1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        opcion = input("Ingresa el número de tu elección (1-3): ")

        if opcion == '1':
            print("\n¡Has elegido el modo Fácil! Ideal para principiantes.")
            break
        elif opcion == '2':
            print("\n¡Has elegido el modo Normal! Un buen desafío para jugadores experimentados.")
            break
        elif opcion == '3':
            print("\n¡Has elegido el modo Difícil! Prepárate para un verdadero reto.")
            break
        else:
            print("\nOpción inválida. Por favor, ingresa un número entre 1 y 3.")

if __name__ == "__main__":
    elegir_dificultad()