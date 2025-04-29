def ingresar_venta(numero_venta):
    """Permite ingresar el monto de una venta."""
    while True:
        venta_str = input(f"Ingrese el monto de la venta {numero_venta}: ")
        if venta_str.replace('.', '', 1).isdigit():
            venta = float(venta_str)
            if venta >= 0:
                return venta
            else:
                print("El monto de la venta debe ser un número positivo.")
        else:
            print("Por favor, ingrese un valor numérico válido.")

def realizar_compra(dia):
    """Pregunta al usuario si desea realizar una compra en el día especificado y, si sí, ingresa el monto."""
    while True:
        opcion = input(f"¿Desea realizar una compra el día {dia}? (s/n): ").lower()
        if opcion == 's':
            while True:
                compra_str = input("Ingrese el monto de la compra: ")
                if compra_str.replace('.', '', 1).isdigit():
                    compra = float(compra_str)
                    if compra >= 0:
                        return compra
                    else:
                        print("El monto de la compra debe ser un número positivo.")
                else:
                    print("Por favor, ingrese un valor numérico válido.")
        elif opcion == 'n':
            return 0
        else:
            print("Por favor, ingrese 's' para sí o 'n' para no.")

def calcular_resultado(total_ventas, total_compras):
    """Calcula la diferencia entre ventas y compras e indica el resultado."""
    diferencia = total_ventas - total_compras
    if diferencia > 0:
        print(f"\n¡Al final de la semana hubo una ganancia de: ${diferencia:.2f}!")
    elif diferencia < 0:
        print(f"\n¡Al final de la semana hubo una pérdida de: ${abs(diferencia):.2f}!")
    else:
        print("\nAl final de la semana no hubo ni ganancia ni pérdida.")

print("Ingrese la información de las 3 ventas:")
ventas = [ingresar_venta(i + 1) for i in range(3)]
total_ventas = sum(ventas)
print(f"\nEl total de ventas de la semana es: ${total_ventas:.2f}")

print("\nIngrese la información de las compras durante la semana:")
total_compras = 0
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for dia in dias_semana:
    compra_dia = realizar_compra(dia)
    total_compras += compra_dia

print(f"\nEl total de compras de la semana es: ${total_compras:.2f}")

calcular_resultado(total_ventas, total_compras)