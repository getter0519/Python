# 1. Función para evaluar si es apto para crear correo electrónico
def es_apto_para_correo(edad):
    return edad >= 18

# 2. Funciones para sumar y restar dos números
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# 3. Función que opera según la opción ingresada
def operar(opcion, a, b):
    if opcion == 1:
        return sumar(a, b)
    elif opcion == 2:
        return restar(a, b)
    else:
        return "Opción inválida"

# 4. Funciones para validar correo y contraseña
def validar_correo(correo):
    return (
        "@" in correo and
        "." in correo and
        ("cl" in correo or "com" in correo)
    )

def validar_contraseña(contraseña):
    return (
        len(contraseña) >= 10 and
        contraseña.isalnum()
    )

# Ejemplo de uso:
# 1. Edad
edad = int(input("Ingrese su edad: "))
if es_apto_para_correo(edad):
    print("Es apto para crearse un correo electrónico.")
else:
    print("No es apto para crearse un correo electrónico.")

# 2 y 3. Sumar o restar según opción
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
opcion = int(input("Elija una opción (1: Sumar, 2: Restar): "))
resultado = operar(opcion, a, b)
print(f"Resultado: {resultado}")

# 4. Validar correo y contraseña con while
while True:
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")
    if validar_correo(correo) and validar_contraseña(contraseña):
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Correo o contraseña inválidos. Intente nuevamente.")