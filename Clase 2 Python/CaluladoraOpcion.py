# Función para sumar dos números
def sumar(num1, num2):
    resultado = num1 + num2
    print(f"La suma de {num1} + {num2} es: {resultado}")

# Función para restar dos números
def restar(num1, num2):
    resultado = num1 - num2
    print(f"La resta de {num1} - {num2} es: {resultado}")

# Función para multiplicar dos números
def multiplicar(num1, num2):
    resultado = num1 * num2
    print(f"La multiplicación de {num1} * {num2} es: {resultado}")

# Función para dividir dos números
def dividir(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división de {num1} / {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")

# Función para mostrar el menú y realizar la operación seleccionada
def calculadora():
    while True:
        print("\nSeleccione la operación que desea realizar:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Adiós!")
            break

        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if opcion == '1':
            sumar(num1, num2)
        elif opcion == '2':
            restar(num1, num2)
        elif opcion == '3':
            multiplicar(num1, num2)
        elif opcion == '4':
            dividir(num1, num2)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Llamamos a la función principal
calculadora()