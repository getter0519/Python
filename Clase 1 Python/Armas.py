def elegir_arma():
    """Pide al usuario que elija una poción y muestra su efecto."""
while True:
    print ("\nElige una poción para usar:")
    print ("1. Arco")
    print ("2. Espada")
    print ("3. Baculo")
    opcion = input("Ingresa el número de tu elección (1-3): ")

    if opcion == '1':
        print("\n!Has elegido el arco")
        break
    elif opcion == '2':
        print("\n!Has elegido la espada")
        break
    elif opcion == '3':
        print("\n!Has elegido el baculo")
        break
    else:
        print("\nOpción inválida. Por favor, ingresa un número entre 1 y 3.")
        
if __name__ == "__main__":
    elegir_arma()