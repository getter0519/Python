def solicitar_numero():
    numero = input("Ingrese un número positivo (0 para terminar): ")
    while not numero.isdigit() and numero != "0":
        print("Entrada no válida. Ingrese solo números positivos.")
        numero = input("Ingrese un número positivo (0 para terminar): ")
    return int(numero)

def acumular_numeros():
    total = 0
    while True:
        numero = solicitar_numero()
        if numero == 0:
            break
        elif numero < 0:
            print("Número No Válido. Intente nuevamente.")
        else:
            total += numero
    print("Total de números positivos acumulados:", total)

acumular_numeros()