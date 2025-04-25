# Definimos la función 'saludar' que solicita al usuario ingresar su nombre.
def saludar():
    # Solicitamos al usuario que ingrese su nombre mediante la función input.
    nombre = input("Ingrese su nombre:")
    # Mostramos un mensaje de saludo personalizado utilizando una f-string.
    print(f"hola {nombre}, Como estas? ")
    # Retornamos el nombre ingresado por el usuario.
    return nombre  

# Llamamos a la función 'saludar' y almacenamos el nombre ingresado en la variable 'nombre_usuario'.
nombre_usuario = saludar()  
# Mostramos un mensaje de despedida utilizando el nombre ingresado por el usuario.
print(f"Adios. {nombre_usuario}")