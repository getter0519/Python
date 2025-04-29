def autenticar():
    print("¿Eres empresa o cliente?")
    usuario = input("Ingrese 'empresa' o 'cliente': ").strip().lower()
    if usuario == "empresa":
        clave = input("Clave empresa: ").strip()
        if clave == "1234":
            return "empresa"
    elif usuario == "cliente":
        clave = input("Clave cliente: ").strip()
        if clave == "abcd":
            return "cliente"
    print("Autenticación fallida.")
    return autenticar()

def mostrar_productos():
    print("\nProductos disponibles para fabricar:")
    print("1. Silla (Madera:4, Clavos:10)")
    print("2. Mesa (Madera:6, Clavos:15)")
    print("3. Estante (Madera:5, Clavos:12, Pintura:1)")

def requerimientos(producto):
    req = {
        "silla": {"Madera": 4, "Clavos": 10},
        "mesa": {"Madera": 6, "Clavos": 15},
        "estante": {"Madera": 5, "Clavos": 12, "Pintura": 1}
    }
    return req[producto]

def fabricar(producto, materia, inventario, historial):
    req = requerimientos(producto)
    for mat, cant in req.items():
        if materia[mat]["stock"] < cant:
            print(f"No hay suficiente {mat}.")
            return
    for mat, cant in req.items():
        materia[mat]["stock"] -= cant
    costo = sum(materia[mat]["costo"] * cant for mat, cant in req.items()) + 5000
    inventario[producto]["stock"] += 1
    inventario[producto]["costo"] = costo
    historial.append(producto)
    print(f"{producto.capitalize()} fabricado. Costo: ${costo}")

def mostrar_stock(materia):
    print("\nStock materia prima:")
    for mat, info in materia.items():
        print(f"{mat}: {info['stock']}")

def mostrar_inventario(inventario):
    print("\nProductos para venta:")
    for prod, info in inventario.items():
        if info["stock"] > 0:
            precio = int(info["costo"] * 1.3)
            print(f"{prod.capitalize()} - Stock: {info['stock']} - Precio: ${precio}")

def vender(inventario, historial_ventas):
    mostrar_inventario(inventario)
    prod = input("¿Qué producto desea comprar?: ").strip().lower()
    if prod in inventario and inventario[prod]["stock"] > 0:
        nombre = input("Ingrese su nombre: ").strip()
        precio = int(inventario[prod]["costo"] * 1.3)
        inventario[prod]["stock"] -= 1
        historial_ventas.append((nombre, prod, precio))
        print(f"¡Gracias {nombre}! Compraste {prod} por ${precio}")
    else:
        print("Producto no disponible.")

def mostrar_historial(historial, historial_ventas):
    print("\nFabricados:", historial)
    print("Vendidos:")
    for venta in historial_ventas:
        print(f"Cliente: {venta[0]}, Producto: {venta[1]}, Precio: ${venta[2]}")

def main():
    materia = {
        "Madera": {"stock": 20, "costo": 500},
        "Clavos": {"stock": 50, "costo": 50},
        "Pintura": {"stock": 10, "costo": 800}
    }
    inventario = {
        "silla": {"stock": 0, "costo": 0},
        "mesa": {"stock": 0, "costo": 0},
        "estante": {"stock": 0, "costo": 0}
    }
    historial = []
    historial_ventas = []

    usuario = autenticar()
    if usuario == "empresa":
        while True:
            mostrar_productos()
            mostrar_stock(materia)
            op = input("Elija producto a fabricar (silla/mesa/estante o Enter para salir): ").strip().lower()
            if op == "":
                break
            if op in inventario:
                fabricar(op, materia, inventario, historial)
            else:
                print("Opción no válida.")
        mostrar_historial(historial, historial_ventas)
    else:
        while True:
            mostrar_inventario(inventario)
            op = input("¿Desea comprar? (silla/mesa/estante o Enter para salir): ").strip().lower()
            if op == "":
                break
            vender(inventario, historial_ventas)
        mostrar_historial(historial, historial_ventas)

main()