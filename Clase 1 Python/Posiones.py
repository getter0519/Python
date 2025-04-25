def usar_poscion():
    """Pide al usuario que elija una poción y muestra su efecto."""
while True:
    print ("\nElige una poción para usar:")
    print ("1. Poción de vida (Rojo)")
    print ("2. Poción de Mana (Azul)")
    print ("3. Pocion de velocidad (Verde)")
    opcion = input("Ingresa el número de tu elección (1-3): ")
    if opcion == '1':
        print("\n!Has usado la pocion roja, Has recuperado vida.")
        break
    elif opcion == '2':
        print("\n!Has usado la pocion azul, Has recuperado mana.")
        break
    elif opcion == '3':
        print("\n!Has usado la pocion verde, Has recuperado velocidad.")
        break
    else:
        print("\nOpción inválida. Por favor, ingresa un número entre 1 y 3.")
        
if __name__ == "__main__":
    usar_poscion()