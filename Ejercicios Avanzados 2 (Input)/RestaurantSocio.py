def es_socio(tipo):
    return tipo.lower() == "socio"

def descuento(monto):
    return monto * 0.9

tipo = input("Tipo de cliente (socio/no socio): ")
monto = float(input("Monto del pedido: "))

if es_socio(tipo):
    print(f"Total con descuento: ${descuento(monto):.2f}")
else:
    print(f"Total sin descuento: ${monto:.2f}")