def verificar_acceso(nivel, tiene_llave):
    if nivel > 15 and tiene_llave.lower() == "sí":
        return True
    else:
        return False

def mostrar_resultado():
    nivel = int(input("Ingresa el nivel de tu personaje: "))
    tiene_llave = input("¿Tienes la llave mágica? (sí o no): ")
    acceso_permitido = verificar_acceso(nivel, tiene_llave)
mostrar_resultado()