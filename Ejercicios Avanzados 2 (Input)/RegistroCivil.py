def validar_nombres(primer_nombre, segundo_nombre):
    def contar_vocales(nombre):
        return sum(1 for letra in nombre.lower() if letra in "aeiou")
    if contar_vocales(primer_nombre) < 2:
        print(f"{primer_nombre} es inválido (por ley debe tener al menos 2 vocales).")
    if contar_vocales(segundo_nombre) < 2:
        print(f"{segundo_nombre} es inválido (por ley debe tener al menos 2 vocales).")
    if contar_vocales(primer_nombre) >= 2 and contar_vocales(segundo_nombre) >= 2:
        print("Ambos nombres son válidos (por ley tienen al menos 2 vocales).")

n1 = input("Primer nombre: ")
n2 = input("Segundo nombre: ")
validar_nombres(n1, n2)