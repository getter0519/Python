def sumar():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"La suma es {a + b}")
    
def restar():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"La resta es {a - b}")

opcion = input("elija una opcion (1:sumar, 2: restar): ")
if opcion == "1":
    sumar()
elif opcion == "2":
    restar()
else:
    print("opcion invalida")
