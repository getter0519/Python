def puede_usar_armadura(nombre, nivel):
    """Verifica si el personaje puede usar la Armadura Legendaria."""
    if nivel >= 10:
        print(f"{nombre} puede usar la Armadura Legendaria.")
    else:
        print(f"{nombre} no puede usar la Armadura Legendaria. Necesita ser al menos nivel 10.")
nombre = input("Ingresa el nombre del personaje: ")
nivel = int(input("Ingresa el nivel del personaje: "))
puede_usar_armadura(nombre, nivel)