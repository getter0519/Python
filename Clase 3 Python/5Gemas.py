def recolectar_gemas():
    gemas = {"roja": 0, "azul": 0, "verde": 0}

    for i in range(5):
        while True:
            color = input(f"Ingrese el color de la gema {i + 1} (Roja, Azul, Verde): ").lower()
            if color in gemas:
                gemas[color] += 1
                break
            print("Color inválido. Por favor, ingresa Roja, Azul o Verde.")

    print("\nResumen de gemas recolectadas:")
    for color, cantidad in gemas.items():
        print(f"Gemas {color}: {cantidad}")

# Llamar a la función principal
recolectar_gemas()