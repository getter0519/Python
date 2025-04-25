def es_apto_para_correo(edad):
    if edad >= 18:
        print("Es apto para correo")
        return True
    else:
        print("No es apto para correo")
        return False
while True:
    edad = int(input("Ingrese su edad: "))
    if es_apto_para_correo(edad):
        break