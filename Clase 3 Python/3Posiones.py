def seleccionar_dificultad():
    print("Selecciona la dificultad del juego:")
    print("1. Fácil")
    print("2. Normal")
    print("3. Difícil")
    
    opcion = input("Ingresa el número de tu elección: ")
    
    if opcion == '1':
        print("Has seleccionado la dificultad Fácil. ¡Buena suerte!")
    elif opcion == '2':
        print("Has seleccionado la dificultad Normal. ¡Prepárate para el desafío!")
    elif opcion == '3':
        print("Has seleccionado la dificultad Difícil. ¡Que comience la batalla!")
    else:
        print("Opción inválida. Se seleccionará la dificultad Normal por defecto.")
        print("Has seleccionado la dificultad Normal. ¡Prepárate para el desafío!")

# Llamar a la función
seleccionar_dificultad()