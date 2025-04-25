def añadir_propina():
    monto = float(input("ingrese el monto del pedido: "))
    propina = monto * 0.10
    total = monto + propina
    print (f"Total sin propina: ${monto:.2f}")
    print (f"Propina sugerida (10%): ${propina:.2f}")
    print (f"Total con propina: ${total:.2f}")
    
añadir_propina()