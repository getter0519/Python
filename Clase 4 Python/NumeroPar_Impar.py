def es_par(numero):
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")
        
es_par(0)