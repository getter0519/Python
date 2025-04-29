import time

def mostrar_productos():
    print("\n+---------+-------+-------+---------+")
    print("| Código  | Silla | Mesa  | Estante |")
    print("+---------+-------+-------+---------+")
    print("| Madera  |   4   |   6   |    5    |")
    print("| Clavos  |  10   |  15   |   12    |")
    print("| Pintura |   -   |   -   |    1    |")
    print("+---------+-------+-------+---------+")

def mostrar_stock(materia_prima):
    print("\nStock actual de materia prima:")
    print("+---------+--------+")
    print("| Material| Stock  |")
    print("+---------+--------+")
    for nombre, info in materia_prima.items():
        print(f"| {nombre:<7} | {info['stock']:^6} |")
    print("+---------+--------+")

def obtener_requerimientos(producto):
    requerimientos = {
        "silla": {"Madera": 4, "Clavos": 10},
        "mesa": {"Madera": 6, "Clavos": 15},
        "estante": {"Madera": 5, "Clavos": 12, "Pintura": 1}
    }
    return requerimientos.get(producto, {})

def verificar_stock(materia_prima, requeridos):
    for mat, cant in requeridos.items():
        if materia_prima[mat]["stock"] < cant:
            print(f"No hay suficiente {mat}. Se requieren {cant}, hay {materia_prima[mat]['stock']}.")
            return False
    return True

def descontar_materia_prima(materia_prima, requeridos):
    for mat, cant in requeridos.items():
        materia_prima[mat]["stock"] -= cant

def calcular_costo_materia_prima(materia_prima, requeridos):
    total = 0
    for mat, cant in requeridos.items():
        total += materia_prima[mat]["costo"] * cant
    return total

def calcular_costo_mano_obra(etapas, costo_mano_obra):
    return len(etapas) * costo_mano_obra

def fabricar_producto(producto, materia_prima, costo_mano_obra):
    etapas = ["Diseño", "Fabricación", "Ensamblado", "Control de calidad", "Terminado"]
    requeridos = obtener_requerimientos(producto)
    if not verificar_stock(materia_prima, requeridos):
        print("No se puede fabricar el producto por falta de materia prima.")
        return

    print("\nIniciando proceso de producción...")
    for etapa in etapas:
        print(f"Etapa: {etapa}")
        time.sleep(1)

    descontar_materia_prima(materia_prima, requeridos)
    costo_mp = calcular_costo_materia_prima(materia_prima, requeridos)
    costo_mo = calcular_costo_mano_obra(etapas, costo_mano_obra)
    costo_total = costo_mp + costo_mo

    print(f"\nProducto fabricado: {producto.capitalize()}")
    time.sleep(1)
    print(f"Costo total de producción: ${costo_total}")
    time.sleep(1)
    mostrar_stock(materia_prima)

def main():
    materia_prima = {
        "Madera": {"stock": 20, "costo": 500},
        "Clavos": {"stock": 50, "costo": 50},
        "Pintura": {"stock": 10, "costo": 800}
    }
    costo_mano_obra = 1000

    while True:
        mostrar_productos()
        mostrar_stock(materia_prima)
        print("\nSeleccione el producto a fabricar:")
        print("1. Silla\n2. Mesa\n3. Estante\nEnter para salir")
        opcion = input("Opción: ").strip()
        if opcion == "":
            print("Saliendo del sistema de producción.")
            break
        if opcion == "1":
            producto = "silla"
        elif opcion == "2":
            producto = "mesa"
        elif opcion == "3":
            producto = "estante"
        else:
            print("Opción no válida.")
            continue
        fabricar_producto(producto, materia_prima, costo_mano_obra)

main()