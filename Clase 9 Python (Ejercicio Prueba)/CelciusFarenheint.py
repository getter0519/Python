def mostrar_menu():
    print("¿A qué unidad desea convertir la temperatura?")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    opcion = input("Seleccione una opción (1 o 2): ").strip()
    return opcion

def leer_temperatura():
    temp = input("Ingrese la temperatura en grados Celsius: ").replace(",", ".").strip()
    if temp.replace('.', '', 1).lstrip('-').isdigit():
        return float(temp)
    else:
        print("Por favor, ingrese un número válido.")
        return leer_temperatura()

def convertir_temperatura():
    opcion = mostrar_menu()
    while opcion not in ['1', '2']:
        print("Opción no válida. Por favor, seleccione 1 o 2.")
        opcion = mostrar_menu()
    celsius = leer_temperatura()
    if opcion == '1':
        resultado = (celsius * 9/5) + 32
        print(f"{celsius}°C es igual a {resultado:.2f} °Fahrenheit.")
    elif opcion == '2':
        resultado = celsius + 273.15
        print(f"{celsius}°C es igual a {resultado:.2f} Kelvin.")

convertir_temperatura()