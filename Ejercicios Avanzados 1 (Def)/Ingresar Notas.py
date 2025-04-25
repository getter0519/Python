def calcular_promedio(total_notas, cantidad_notas):
    if cantidad_notas > 0:
        promedio = total_notas / cantidad_notas
        print(f"\nTotal de notas ingresadas: {cantidad_notas}")
        print(f"Promedio de las notas: {promedio:.2f}")
    else:
        print("\nNo se ingresaron notas válidas.")

def ingresar_notas():
    total_notas = 0
    cantidad_notas = 0
    nota = None  # Inicializamos la variable para entrar al bucle

    print("Ingrese las notas de los alumnos. Ingrese 0 para finalizar.")
    
    while nota != 0:
        try:
            nota = float(input("Ingrese una nota: "))
            
            if nota < 0:
                print("Nota Inválida. Por favor, ingrese un número válido.")
                continue
            
            if nota != 0:
                total_notas += nota
                cantidad_notas += 1
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

    calcular_promedio(total_notas, cantidad_notas)

# Llamar a la función principal
ingresar_notas()
