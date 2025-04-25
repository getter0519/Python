def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

f = float(input("Ingrese la temperatura en grados Fahrenheit: "))
c = fahrenheit_a_celsius(f)
print(f"{f}°F equivalen a {c:.2f}°C")