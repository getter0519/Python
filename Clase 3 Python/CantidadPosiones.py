def calcular_total_posiones(cantidad_rojas, cantidad_azules, cantidad_verdes):
    precio_roja = 10
    precio_azul = 15
    precio_verde = 20

    total_rojas = cantidad_rojas * precio_roja
    total_azules = cantidad_azules * precio_azul
    total_verdes = cantidad_verdes * precio_verde

    total = total_rojas + total_azules + total_verdes
    return total

def comprar_posiones():
    print("Precios de pociones:")
    print("Poción roja: 10 monedas")
    print("Poción azul: 15 monedas")
    print("Poción verde: 20 monedas")
    
    while True:
        cantidad_rojas = int(input("¿Cuántas pociones rojas deseas comprar? "))
        if cantidad_rojas >= 0:
            break
        print("La cantidad no puede ser negativa. Inténtalo de nuevo.")
    
    while True:
        cantidad_azules = int(input("¿Cuántas pociones azules deseas comprar? "))
        if cantidad_azules >= 0:
            break
        print("La cantidad no puede ser negativa. Inténtalo de nuevo.")
    
    while True:
        cantidad_verdes = int(input("¿Cuántas pociones verdes deseas comprar? "))
        if cantidad_verdes >= 0:
            break
        print("La cantidad no puede ser negativa. Inténtalo de nuevo.")
    
    total = calcular_total_posiones(cantidad_rojas, cantidad_azules, cantidad_verdes)
    print(f"El total a pagar es: {total} monedas.")

comprar_posiones()