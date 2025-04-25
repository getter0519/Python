
try:
    misiones = int(input("¿Cuántas misiones has completado? "))
    if misiones < 0:
        print("El número de misiones no puede ser negativo.")
    else:
       
        recompensa_total = misiones * 100
        calculo_detalle = f"({misiones} x 100 monedas"
        if misiones > 5:
            recompensa_total += 500
            calculo_detalle += " + 500 bonus" 

        calculo_detalle += ")" 

       
        print(f"\nTotal ganado: {recompensa_total} monedas {calculo_detalle}")

except ValueError:
    
    print("Entrada inválida. Por favor, ingresa un número entero.")
