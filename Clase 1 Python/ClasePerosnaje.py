
clase = input("¿Cuál es tu clase? (guerrero, arquero, mago): ").lower()

arma = input("¿Qué arma has elegido? (espada, arco, báculo): ").lower()


compatible = False

if clase == "guerrero" and arma == "espada":
    compatible = True
elif clase == "arquero" and arma == "arco":
    compatible = True
elif clase == "mago" and arma == "báculo": 
    compatible = True


if compatible:
    print(f"\n¡Válido! Un {clase} puede usar {arma}.")
else:
    
    print(f"\n¡Inválido! Un {clase} no puede usar {arma} según las reglas.")

