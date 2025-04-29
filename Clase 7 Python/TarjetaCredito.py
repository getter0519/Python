def solicitar_precio():
    precio = input("Ingrese el precio del producto (o Enter para finalizar): ").strip()
    if precio == "":
        return ""
    if precio.isdigit() and int(precio) > 0:
        return int(precio)
    else:
        print("Ingrese un precio válido (número positivo).")
        return solicitar_precio()

def solicitar_medio_pago():
    print("\nSeleccione medio de pago:")
    print("1. Efectivo")
    print("2. Tarjeta de crédito")
    print("3. Tarjeta de débito")
    medio = input("Ingrese 1, 2 o 3: ").strip()
    if medio in ["1", "2", "3"]:
        return medio
    else:
        print("Opción no válida.")
        return solicitar_medio_pago()

def calcular_total(total, medio):
    if medio == "1":  # Efectivo
        total = total * 0.19
    elif medio == "2":  # Crédito
        total = total * 0.9
    elif medio == "3":  # Débito
        total = total * 0.5 + 3000
    return total

def main():
    total = 0
    cantidad = 0
    precio = solicitar_precio()
    while precio != "":
        total += precio
        cantidad += 1
        precio = solicitar_precio()
    print("Cantidad de productos ingresados:", cantidad)
    print("Suma total de los precios:", total)

    if cantidad > 0:
        medio = solicitar_medio_pago()
        total_final = calcular_total(total, medio)
        print(f"Total a pagar según medio de pago: {round(total_final, 2)}")

main()  