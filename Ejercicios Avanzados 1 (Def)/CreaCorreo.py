def Crear_correo():
    while True:
        correo = input("Ingrese su correo: ").strip()
        if "@" in correo and (correo.endswith(".com") or correo.endswith(".cl")) and ("gmail" in correo or "hotmail" in correo):
            print("¡Correo creado con éxito!")
            print(f"Su correo es: {correo}")
            break
        print("Correo inválido. Asegúrese de que contenga '@', termine en '.com' o '.cl' y contenga 'gmail' o 'hotmail'.")

# Llamar a la función principal
Crear_correo()