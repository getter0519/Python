# Pide el nivel del jugador
try:
    nivel_jugador = int(input("¿Cuál es tu nivel actual? "))

    # Pide si tiene la llave mágica y convierte la respuesta a minúsculas
    respuesta_llave = input("¿Tienes la llave mágica? (sí/no): ").lower()

    # Verifica si tiene la llave (asume 'sí' si empieza con 's' o 'y')
    tiene_llave = respuesta_llave.startswith('s') or respuesta_llave.startswith('y')

    # Comprueba si cumple ambas condiciones: nivel > 15 Y tiene_llave
    if nivel_jugador > 15 and tiene_llave:
        print("\n¡Puedes entrar!")
    else:   
        
        # Mensaje genérico si no cumple una o ambas condiciones
        print("\nNo puedes entrar. Necesitas nivel mayor a 15 Y la llave mágica.")

except ValueError:
    # Mensaje si no ingresa un número para el nivel
    print("Entrada de nivel inválida. Por favor, ingresa un número entero.")

