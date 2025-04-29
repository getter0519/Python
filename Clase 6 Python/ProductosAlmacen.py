def solicitar_producto():
    producto = input("Ingrese el nombre de un producto (o presione Enter para finalizar): ").strip()
    return producto

def contar_variedad_productos():
    productos = set()
    contador = 0
    while True:
        producto = solicitar_producto()
        if producto == "":
            break
        if producto not in productos:
            productos.add(producto)
            contador += 1
    print("Variedad total de productos en el almacén:", contador)

contar_variedad_productos()