def mostrar_productos(productos):
    print("\nProductos disponibles:")
    for codigo, info in productos.items():
        print(f"{codigo}: {info['nombre']} - ${info['precio']} (Stock: {info['stock']})")

def seleccionar_producto():
    return input("Ingrese el código del producto (o 'fin' para terminar): ").strip()

def solicitar_cantidad():
    cantidad = input("¿Cuántas unidades desea?: ").strip()
    if cantidad.isdigit() and int(cantidad) > 0:
        return int(cantidad)
    print("Cantidad no válida.")
    return solicitar_cantidad()

def agregar_al_carrito(productos, carrito, codigo, cantidad):
    if productos[codigo]['stock'] >= cantidad:
        if codigo in carrito:
            carrito[codigo] += cantidad
        else:
            carrito[codigo] = cantidad
        productos[codigo]['stock'] -= cantidad
        print("Producto agregado al carrito.")
    else:
        print("Stock insuficiente.")

def eliminar_del_carrito(productos, carrito):
    codigo = input("Código del producto a eliminar: ").strip()
    if codigo in carrito:
        productos[codigo]['stock'] += carrito[codigo]
        del carrito[codigo]
        print("Producto eliminado del carrito.")
    else:
        print("Ese producto no está en el carrito.")

def calcular_total(productos, carrito):
    total = 0
    total_items = 0
    for codigo, cantidad in carrito.items():
        total += productos[codigo]['precio'] * cantidad
        total_items += cantidad
    descuento = 0
    if total_items > 5:
        descuento = total * 0.10
        total -= descuento
    return total, descuento

def mostrar_boleta(nombre, productos, carrito, total, descuento, metodo_pago):
    print("\n--- BOLETA ---")
    print(f"Cliente: {nombre}")
    for codigo, cantidad in carrito.items():
        print(f"{productos[codigo]['nombre']} x{cantidad} - ${productos[codigo]['precio']} c/u")
    if descuento > 0:
        print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print(f"Método de pago: {metodo_pago}")

def seleccionar_metodo_pago():
    metodo = input("Método de pago (Efectivo/Tarjeta): ").strip().capitalize()
    if metodo in ["Efectivo", "Tarjeta"]:
        return metodo
    print("Método no válido.")
    return seleccionar_metodo_pago()

def main():
    productos = {
        "1": {"nombre": "Coca-Cola", "precio": 1200, "stock": 10},
        "2": {"nombre": "Pepsi", "precio": 1100, "stock": 8},
        "3": {"nombre": "Red Bull", "precio": 1800, "stock": 5},
        "4": {"nombre": "Agua", "precio": 900, "stock": 15}
    }
    carrito = {}
    nombre = input("Ingrese su nombre: ").strip()

    while True:
        mostrar_productos(productos)
        print("\nOpciones: [1] Agregar producto [2] Eliminar producto [3] Finalizar compra")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            codigo = seleccionar_producto()
            if codigo == "fin":
                continue
            if codigo in productos:
                cantidad = solicitar_cantidad()
                agregar_al_carrito(productos, carrito, codigo, cantidad)
            else:
                print("Código no válido.")
        elif opcion == "2":
            eliminar_del_carrito(productos, carrito)
        elif opcion == "3":
            if not carrito:
                print("El carrito está vacío.")
                continue
            total, descuento = calcular_total(productos, carrito)
            metodo_pago = seleccionar_metodo_pago()
            mostrar_boleta(nombre, productos, carrito, total, descuento, metodo_pago)
            break
        else:
            print("Opción no válida.")

main()