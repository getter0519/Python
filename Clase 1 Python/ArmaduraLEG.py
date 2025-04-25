nombre = input ("ingrese el nombre de su personaje: ")
while True:
    nivel_str = input("¿Cuál es el nivel de tu personaje? :")
    if nivel_str.isdigit():
        nivel_personaje = int(nivel_str)
        if nivel_personaje > 0:
            break 
        else:
            print("El nivel debe ser un número mayor que 0. Inténtalo de nuevo.")
    else:
        print("Eso no parece un número entero. Inténtalo de nuevo.")
nivel_requerido = 10
if nivel_personaje >= nivel_requerido:
    print(f"\n¡Genial, {nombre}! Tu nivel ({nivel_personaje}) te permite usar la Armadura Legendaria.")
else:
    print(f"\nLo siento, {nombre}. Necesitas alcanzar el nivel {nivel_requerido} para usar la Armadura Legendaria. Tu nivel actual es {nivel_personaje}.")