def solicitar_precio():
    precio = input("Ingrese el precio del producto (o Enter para finalizar): ").strip()
    if precio == "":
        return ""
    if precio.isdigit() and int(precio) > 0:
        return int(precio)
    else:
        print("Ingrese un precio válido (número positivo).")
        return solicitar_precio()

def sumar_precios():
    total = 0
    cantidad = 0
    precio = solicitar_precio()
    while precio != "":
        total += precio
        cantidad += 1
        precio = solicitar_precio()
    print("Cantidad de productos ingresados:", cantidad)
    print("Suma total de los precios:", total)

sumar_precios()