def es_vocal():
    letra = input("Ingrese una letra: ").lower()
    if letra in 'aeiou':
        print(f"{letra} es una vocal.")
    else:
        print(f"{letra} no es una vocal.")
es_vocal()