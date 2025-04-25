def sumar_o_restar(op):
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    if op == "suma":
        return a + b
    elif op == "resta":
        return a - b
    else:
        return "Opción inválida"

opcion = input("¿Qué desea hacer? (suma/resta): ").strip().lower()
resultado = sumar_o_restar(opcion)
print("Resultado:", resultado)