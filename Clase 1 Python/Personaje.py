def crear_personaje():
    """Permite al usuario crear su personaje y muestra sus datos."""

    print("¡Crea tu personaje!")

    nombre = input("Elige un nombre para tu personaje: ")

    while True:
        clase = input("Elige una clase (guerrero, mago o arquero): ").lower()
        if clase in ["guerrero", "mago", "arquero"]:
            break
        else:
            print("Clase inválida. Por favor, elige entre guerrero, mago o arquero.")

    while True:
        try:
            nivel = int(input("Elige un nivel inicial (número entero): "))
            if nivel > 0:
                break
            else:
                print("El nivel debe ser un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    print("\n--- Datos del Personaje ---")
    print(f"a. ¡Bienvenido, {nombre}!")
    print(f"b. Clase: {clase.capitalize()}")
    print(f"c. Nivel: {nivel}")
    print("d. ¡Prepárate para la aventura!")

crear_personaje()