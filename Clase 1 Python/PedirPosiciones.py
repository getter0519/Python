# Precios de las pociones
precio_roja = 50
precio_azul = 60
precio_verde = 55
precio_elegido = 0

# Pide la cantidad (intenta convertir a número)
try:
    cantidad = int(input("¿Cuántas pociones quieres comprar? "))

    # Pide el tipo de poción (convierte a minúsculas)
    tipo = input("¿Qué tipo de poción? (roja, azul, verde): ").lower()

    if tipo == "roja":
        precio_elegido = precio_roja
    elif tipo == "azul":
        precio_elegido = precio_azul
    elif tipo == "verde":
        precio_elegido = precio_verde
    else:
        # Si el tipo no es válido, informa y el precio sigue en 0
        print("Tipo de poción no válido.")

    # Calcula y muestra el total solo si la cantidad y el precio son válidos
    if cantidad > 0 and precio_elegido > 0:
        costo_total = cantidad * precio_elegido
        print(f"\nTotal a pagar por {cantidad} pociones tipo '{tipo}': {costo_total} monedas.")
    elif cantidad <= 0:
        print("\nDebes comprar al menos 1 poción.")
    # Si el precio es 0, ya se mostró el mensaje de tipo inválido

except ValueError:
    # Mensaje si la cantidad no fue un número
    print("Cantidad inválida. Por favor, ingresa un número.")
