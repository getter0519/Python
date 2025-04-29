def ingresar_estudiante():
    nombre = input("Ingrese el nombre del estudiante (o Enter para finalizar): ").strip()
    return nombre

def ingresar_notas():
    notas = []
    cantidad = input("¿Cuántas notas desea ingresar?: ").strip()
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
    else:
        print("Ingrese un número válido mayor a 0.")
        return ingresar_notas()
    for i in range(cantidad):
        nota = input(f"Ingrese la nota {i+1}: ").replace(",", ".").strip()
        if nota.replace('.', '', 1).isdigit():
            nota_float = float(nota)
            if 1.0 <= nota_float <= 7.0:
                notas.append(nota_float)
            else:
                print("La nota debe estar entre 1.0 y 7.0.")
                return ingresar_notas()
        else:
            print("Ingrese un valor numérico válido.")
            return ingresar_notas()
    return notas

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def clasificar_rendimiento(promedio):
    if promedio >= 6.0:
        return "Excelente"
    elif promedio >= 5.0:
        return "Bueno"
    elif promedio >= 4.0:
        return "Regular"
    else:
        return "Insuficiente"

def mostrar_resumen(estudiantes):
    print("\n--- Resumen de Estudiantes ---")
    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        clasificacion = clasificar_rendimiento(promedio)
        print(f"{nombre}: Notas: {notas} | Promedio: {promedio:.2f} | Rendimiento: {clasificacion}")

def buscar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante a buscar: ").strip()
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        promedio = calcular_promedio(notas)
        clasificacion = clasificar_rendimiento(promedio)
        print(f"{nombre}: Notas: {notas} | Promedio: {promedio:.2f} | Rendimiento: {clasificacion}")
    else:
        print("Estudiante no encontrado.")

def editar_nota(estudiantes):
    nombre = input("Ingrese el nombre del estudiante para editar una nota: ").strip()
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        print(f"Notas actuales de {nombre}: {notas}")
        indice = input(f"Ingrese el número de nota a editar (1 a {len(notas)}): ").strip()
        if indice.isdigit() and 1 <= int(indice) <= len(notas):
            indice = int(indice) - 1
            nueva_nota = input("Ingrese la nueva nota: ").replace(",", ".").strip()
            if nueva_nota.replace('.', '', 1).isdigit():
                nueva_nota_float = float(nueva_nota)
                if 1.0 <= nueva_nota_float <= 7.0:
                    notas[indice] = nueva_nota_float
                    estudiantes[nombre] = notas
                    print("Nota actualizada.")
                else:
                    print("La nota debe estar entre 1.0 y 7.0.")
            else:
                print("Ingrese un valor numérico válido.")
        else:
            print("Índice no válido.")
    else:
        print("Estudiante no encontrado.")

def main():
    estudiantes = {}
    while True:
        nombre = ingresar_estudiante()
        if nombre == "":
            break
        notas = ingresar_notas()
        estudiantes[nombre] = notas

    while True:
        print("\nOpciones: [1] Mostrar resumen [2] Buscar estudiante [3] Editar nota [4] Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            mostrar_resumen(estudiantes)
        elif opcion == "2":
            buscar_estudiante(estudiantes)
        elif opcion == "3":
            editar_nota(estudiantes)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

main()