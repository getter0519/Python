def pedir_numero_y_multiplicar_hasta_50():
    numero = input("Ingrese un número entero positivo: ")
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        for i in range(1, 51):
            print(f"{numero} x {i} = {numero * i}")
    else:
        print("El valor ingresado no es un número entero positivo. Intente nuevamente.")
        pedir_numero_y_multiplicar_hasta_50()
        return
pedir_numero_y_multiplicar_hasta_50()