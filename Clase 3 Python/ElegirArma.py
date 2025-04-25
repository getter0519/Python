def elegir_arma():
    print("Elige tu arma:")
    print("1. Espada")
    print("2. Arco")
    print("3. Báculo")

    eleccion = input("Ingresa el número de tu elección: ")

    if eleccion == "1":
        print("Has elegido la Espada. ¡Prepárate para el combate cuerpo a cuerpo!")
    elif eleccion == "2":
        print("Has elegido el Arco. ¡Dispara con precisión desde la distancia!")
    elif eleccion == "3":
        print("Has elegido el Báculo. ¡Usa la magia para derrotar a tus enemigos!")
    else:
        print("Opción inválida. Se te asignará la Espada por defecto.")
        
elegir_arma()