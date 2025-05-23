def ingresar_año():
    año = input ("Ingrese un año (o Enter para finalizar): ").strip()
    if año.isdigit() and int (año) >= 0:
        return int(año)
    else:
        print("Año no válido. Intente nuevamente.")
        return ingresar_año()

def es_bisiesto(año):
    if ( año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

def main ():
    año = ingresar_año()
    if es_bisiesto(año):
        print(f"{año} es un año bisiesto.")
    else:   
        print(f"{año} no es un año bisiesto.")

main()