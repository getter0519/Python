productos = {
    "A1": {"nombre": "Polera", "precio": 8000, "stock": 10},
    "B2": {"nombre": "Pantalón", "precio": 15000, "stock": 8},
    "C3": {"nombre": "Zapatos", "precio": 25000, "stock": 5},
    "D4": {"nombre": "Gorro", "precio": 4000, "stock": 12}
}

def mostrar_productos():
    print("\nProductos disponibles:")
    for c, p in productos.items():
        print(f"{c}: {p['nombre']} - ${p['precio']} (Stock: {p['stock']})")

def seleccionar_producto():
    cod = input("Código producto (fin=terminar, elim=eliminar): ").upper()
    return cod

def verificar_stock(cod, cant):
    return cant <= productos[cod]["stock"]

def agregar_al_carrito(carrito, cod, cant):
    carrito[cod] = carrito.get(cod, 0) + cant

def eliminar_del_carrito(carrito):
    elim = input("Código a eliminar: ").upper()
    if elim in carrito:
        carrito.pop(elim)
        print("Producto eliminado del carrito.")
    else:
        print("Ese producto no está en el carrito.")

def calcular_total(carrito):
    total = sum(productos[c]["precio"] * q for c, q in carrito.items())
    cantidad = sum(carrito.values())
    descuento = 0
    if cantidad > 5:
        descuento = total * 0.1
        total *= 0.9
    return total, descuento

def seleccionar_metodo_pago():
    print("\nMétodos de pago disponibles:")
    print("1. Efectivo")
    print("2. Tarjeta")
    metodo = input("Seleccione el método de pago (1/2): ")
    if metodo == "1":
        return "Efectivo"
    elif metodo == "2":
        return "Tarjeta"
    else:
        return "Desconocido"

def mostrar_boleta(nombre, carrito, total, descuento, metodo_pago):
    print("\n--- BOLETA ---")
    print(f"Cliente: {nombre}")
    for c, q in carrito.items():
        print(f"{productos[c]['nombre']} x{q} - ${productos[c]['precio']} c/u")
    if descuento > 0:
        print(f"Descuento aplicado: -${descuento:.0f}")
    print(f"Total a pagar: ${total:.0f}")
    print(f"Método de pago: {metodo_pago}")

def actualizar_stock(carrito):
    for c, q in carrito.items():
        productos[c]["stock"] -= q

while True:
    nombre = input("Nombre del cliente: ")
    carrito = {}

    while True:
        mostrar_productos()
        cod = seleccionar_producto()
        if cod == "FIN":
            break
        if cod == "ELIM":
            eliminar_del_carrito(carrito)
            continue
        if cod not in productos:
            print("Código inválido.")
            continue
        cant = input("Cantidad: ")
        # Validar que la cantidad sea un número entero positivo sin usar try/except
        while not (cant.isnumeric() and int(cant) > 0):
            print("Cantidad inválida.")
            cant = input("Cantidad: ")
        cant = int(cant)
        if not verificar_stock(cod, cant):
            print("No hay suficiente stock.")
            continue
        agregar_al_carrito(carrito, cod, cant)

    if carrito:
        total, descuento = calcular_total(carrito)
        if descuento > 0:
            print("Descuento aplicado por más de 5 ítems.")
        metodo_pago = seleccionar_metodo_pago()
        mostrar_boleta(nombre, carrito, total, descuento, metodo_pago)
        actualizar_stock(carrito)
    else:
        print("No hay productos en el carrito.")

    otra = input("\n¿Desea realizar otra compra? (s/n): ").lower()
    if otra != "s":
        print("¡Gracias por usar el sistema de ventas!")
        break