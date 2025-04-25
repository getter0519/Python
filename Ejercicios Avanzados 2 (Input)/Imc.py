def calcular_imc_de():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Su índice de masa corporal es: {imc:.2f}")
    if imc < 18.5:
        print("Está delgado.")
    elif 18.5 <= imc < 25:
        print("Está normal.")
    elif 25 <= imc < 30:
        print("Está con sobrepeso.")
    elif 30 <= imc < 40:
        print("Está obeso.")
    else:
        print("Está con obesidad mórbida.")

calcular_imc_de()