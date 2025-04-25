def crear_personaje():
    
    # Solicitar datos al usuario
    print ("¡Bienvenido a la creación de personajes!")
    nombre = input("Ingresa el nombre de tu personaje: ")
    
    #Selecccion de Clase
    print("\nSelecciona una clase para tu personaje:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    
    #Validar la opción de clase
    clase_opcion = input("Ingresa el número de tu elección (1-3): ")
    if clase_opcion == '1':
        clase = "Guerrero"
    elif clase_opcion == '2':
        clase = "Mago"
    elif clase_opcion == '3':
        clase = "Arquero"
    else:
        print("Opción inválida. Se asignará la clase Guerrero por defecto.")
        clase = "Guerrero"
    
    # Selección de nivel
    nivel = int (input("Ingresa el nivel de tu personaje (1-100): "))
    if nivel < 1 or nivel > 100:
        print("Nivel inválido. Se asignará el nivel 1 por defecto.")
        nivel = 1
    return nombre, clase, nivel
# Mostrar bienvenida y detalles del personaje
def mostrar_bienvenida(nombre, clase, nivel):
    print(f"\n¡Bienvenido, {nombre}!")
    print(f"Eres un {clase} de nivel {nivel}. ¡Buena suerte en tu aventura!")
    print("¡Que comience la aventura!")

nombre, clase, nivel = crear_personaje()
mostrar_bienvenida(nombre, clase, nivel)
