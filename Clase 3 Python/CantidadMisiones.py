def calcular_recompensa(misiones):
    recompensa_por_mision = 100
    bonificacion = 500 if misiones > 5 else 0
    total_ganado = (misiones * recompensa_por_mision) + bonificacion
    return total_ganado

def mostrar_resultado():
    misiones = int(input("Ingresa la cantidad de misiones completadas: "))
    total_ganado = calcular_recompensa(misiones)
    print(f"Has completado {misiones} misiones.")
    print(f"Total ganado: {total_ganado} monedas.")

# Llamar a la función principal
mostrar_resultado()