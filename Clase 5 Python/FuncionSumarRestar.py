def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b

while True:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("La suma es:", sumar(num1, num2))
    print("La resta es:", restar(num1, num2))
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    while continuar.lower() not in ['s', 'n']:
        continuar = input("Entrada no válida. ¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() == 'n':
        break