def es_numero_primo():
    n = int(input("Ingrese un número: "))
    if n < 2:
        print("No es primo.")
        return
    for i in range(2, n):
        if n % i == 0:
            print("No es primo.")
            return
    print("Es primo.")

es_numero_primo()