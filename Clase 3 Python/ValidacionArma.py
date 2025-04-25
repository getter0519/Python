def es_arma_valida(clase, arma):
    if clase.lower() == "guerrero" and arma.lower() == "espada":
        return True
    elif clase.lower() == "mago" and arma.lower() == "báculo":
        return True
    elif clase.lower() == "arquero" and arma.lower() == "arco":
        return True
    return False

def verificar_compatibilidad():
    clase = input("Ingresa la clase de tu personaje (Guerrero, Mago, Arquero): ")
    arma = input("Ingresa el arma elegida (Espada, Báculo, Arco): ")
    
    if es_arma_valida(clase, arma):
        print(f"El arma {arma} es compatible con la clase {clase}.")
    else:
        print(f"El arma {arma} no es compatible con la clase {clase}.")

# Llamar a la función principal
verificar_compatibilidad()