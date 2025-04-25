def es_multiplo_de_5(numero):
    numero = int(input("Ingrese un número: "))
    if numero % 5 == 0:
        print(f"{numero} es múltiplo de 5.")
    else:
        print(f"{numero} no es múltiplo de 5.")
es_multiplo_de_5(0)