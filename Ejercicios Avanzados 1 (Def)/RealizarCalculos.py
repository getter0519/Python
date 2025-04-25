import math

numero = 10

def RealizarCalculoSeno(minumero):
    return math.sin(minumero)

def RealizarCalculoFactorial(minumero):
    return math.factorial(minumero)

def RealizarCalculoCoseno(minumero):
    return math.cos(minumero)

print(f"El seno de ({numero}) es: {RealizarCalculoSeno(numero)}")
print(f"El factorial de ({numero}) es: {RealizarCalculoFactorial(numero)}")
print(f"El coseno de ({numero}) es: {RealizarCalculoCoseno(numero)}")