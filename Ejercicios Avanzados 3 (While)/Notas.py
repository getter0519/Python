def ingresar_notas():
    notas = []
    n = int(input("¿Cuántas notas desea ingresar? (mínimo 3): "))
    while n < 3:
        n = int(input("Debe ingresar al menos 3 notas: "))
    for i in range(n):
        nota = float(input(f"Ingrese nota {i+1}: "))
        while not (1.0 <= nota <= 7.0):
            print("Nota fuera de rango.")
            nota = float(input(f"Ingrese nota {i+1}: "))
        notas.append(nota)
    return notas

def promedio(notas):
    return sum(notas) / len(notas)

def clasificar(prom):
    if prom >= 6.0:
        return "Excelente"
    elif prom >= 5.0:
        return "Bueno"
    elif prom >= 4.0:
        return "Regular"
    else:
        return "Insuficiente"

estudiantes = {}

while True:
    print("\n1. Registrar estudiante\n2. Mostrar resumen\n3. Buscar estudiante\n4. Editar nota\n5. Salir")
    op = input("Opción: ")
    if op == "1":
        nombre = input("Nombre del estudiante: ")
        estudiantes[nombre] = ingresar_notas()
    elif op == "2":
        for nombre, notas in estudiantes.items():
            prom = promedio(notas)
            print(f"{nombre}: Notas: {notas} | Promedio: {prom:.2f} | {clasificar(prom)}")
    elif op == "3":
        nombre = input("Nombre a buscar: ")
        if nombre in estudiantes:
            notas = estudiantes[nombre]
            prom = promedio(notas)
            print(f"{nombre}: Notas: {notas} | Promedio: {prom:.2f} | {clasificar(prom)}")
        else:
            print("No encontrado.")
    elif op == "4":
        nombre = input("Nombre del estudiante: ")
        if nombre in estudiantes:
            notas = estudiantes[nombre]
            print(f"Notas actuales: {notas}")
            idx = int(input(f"¿Qué nota desea editar? (1-{len(notas)}): ")) - 1
            if 0 <= idx < len(notas):
                nueva = float(input("Nueva nota: "))
                while not (1.0 <= nueva <= 7.0):
                    print("Nota fuera de rango.")
                    nueva = float(input("Nueva nota: "))
                notas[idx] = nueva
                print("Nota actualizada.")
            else:
                print("Índice inválido.")
        else:
            print("No encontrado.")
    elif op == "5":
        break
    else:
        print("Opción inválida.")