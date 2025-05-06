def leer_valor(mensaje):
    valor = input (mensaje).replace(",", ".").strip()
    if valor.replace('.', '', 1).lstrip('-').isdigit():
        return float(valor)
    else:
        print("Por favor, ingrese un número válido.")
        return leer_valor(mensaje)
    
def calcular_precio_final(precio, descuento):
    return precio - (precio * (descuento / 100))
    
def main():
    precio = leer_valor("Ingrese el precio original: ")
    descuento = leer_valor("Ingrese el porcentaje de descuento: ")
    precio_final = calcular_precio_final(precio, descuento)
    print(f"El precio final después de aplicar el descuento es: {precio_final:.2f}")
    
main()