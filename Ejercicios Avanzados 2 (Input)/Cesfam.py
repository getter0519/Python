def calcular_porcentajes(ninios, adultos, adultos_mayores):
    total = ninios + adultos + adultos_mayores
    if total == 0:
        print("No hay datos para calcular porcentajes.")
        return
    print(f"Porcentaje de niños: {ninios / total * 100:.2f}%")
    print(f"Porcentaje de adultos: {adultos / total * 100:.2f}%")
    print(f"Porcentaje de adultos mayores: {adultos_mayores / total * 100:.2f}%")

ninios = int(input("Ingrese el total de niños: "))
adultos = int(input("Ingrese el total de adultos: "))
adultos_mayores = int(input("Ingrese el total de adultos mayores: "))

calcular_porcentajes(ninios, adultos, adultos_mayores)  