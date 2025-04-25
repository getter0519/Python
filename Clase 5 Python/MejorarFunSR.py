def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def operar_opcion(opcion, a, b):
    if opcion == 1:
        return f"La suma es: {sumar(a, b)}"
    elif opcion == 2:
        return f"La resta es: {restar(a, b)}"
    else:
        return "Opción inválida."

while True:
    opcion = int(input("Elija una opción (1: Sumar, 2: Restar): "))
    if opcion not in (1, 2):
        print("Opción inválida.")
        continue
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(operar_opcion(opcion, num1, num2))
    continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
    while continuar not in ('s', 'n'):
        continuar = input("Por favor, ingrese 's' para sí o 'n' para no: ").lower()
    if continuar == 'n':
        break