def es_devisible():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 == 0:
        print("No se puede dividir por cero.")
    elif num1 % num2 == 0:
        print(f"{num1} es divisible por {num2}.")
    else:
        print(f"{num1} no es divisible por {num2}.")
es_devisible()
