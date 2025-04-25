
try:
    experiencia_actual = int(input("¿Cuánta experiencia tienes actualmente? "))

    experiencia_necesaria = int(input("¿Cuánta experiencia necesitas para subir de nivel? "))

    if experiencia_actual >= experiencia_necesaria:
        print("\n¡Felicidades! Has subido de nivel.")
    else:

        experiencia_faltante = experiencia_necesaria - experiencia_actual
        print(f"\nAún necesitas {experiencia_faltante} puntos de experiencia para subir de nivel.")

except ValueError:

    print("Entrada inválida. Por favor, ingresa números enteros para la experiencia.")
