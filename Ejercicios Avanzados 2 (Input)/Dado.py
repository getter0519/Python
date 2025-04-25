import random

def verificar_numero(n):
    return 1 <= n <= 6

def lanzar_dado():
    return random.randint(1, 6)

numero = int(input("Ingrese un número del 1 al 6: "))
if not verificar_numero(numero):
    print("Número inválido. Debe ser entre 1 y 6.")
else:
    dado = lanzar_dado()
    print(f"El dado cayó en: {dado}")
    if dado == numero:
        print("¡Acertó!")
    else:
        print("No acertó.") 