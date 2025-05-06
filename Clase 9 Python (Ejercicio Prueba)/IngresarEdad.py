def ingresar_edad():
    edad = input ("Ingrese su edad: ").strip()
    if edad.isdigit()and int (edad) >= 0:
        return int(edad)
    else:
        print("Edad no válida. Intente nuevamente.")
        return ingresar_edad()

def clasificar_edad(edad):
    if 0 <= edad <= 12:
        return "Niño"
    elif 13 <= edad <= 17:
        return "Adolescente"
    elif 18 <= edad <= 64:
        return "Adulto"
    elif edad <= 65:
        return "Adulto Mayor"
    elif edad >= 66 and edad < 120:
        return "Ancianno longevo"
    elif edad >= 121:
        return "Ancianno inmortal"
    else:
        return "Edad no válida"
    
def main():
    edad = ingresar_edad()
    clasificacion = clasificar_edad(edad)
    print(f"Edad: {edad}, Clasificación: {clasificacion}")

main()