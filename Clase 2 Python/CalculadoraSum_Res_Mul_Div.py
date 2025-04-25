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

# Función para ingresar dos números y realizar las operaciones
def ingresar_numeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    # Llamamos a las funciones de operaciones con los números ingresados
    sumar(num1, num2)
    restar(num1, num2)
    multiplicar(num1, num2)
    dividir(num1, num2)

# Llamamos a la función principal
ingresar_numeros()