
gemas_rojas = 0
gemas_azules = 0
gemas_verdes = 0
gemas_otras = 0 

print("Recolecta 5 gemas. Indica el color de cada una.")

for i in range(5):

    color_gema = input(f"Color de la gema #{i+1} (roja, azul, verde): ").lower()

    if color_gema == "roja":
        gemas_rojas += 1
    elif color_gema == "azul":
        gemas_azules += 1
    elif color_gema == "verde":
        gemas_verdes += 1
    else:

        gemas_otras += 1
        print("(Color no reconocido, contado como 'otra')") 


print("\n--- Recuento Final de Gemas ---")
print(f"Gemas Rojas: {gemas_rojas}")
print(f"Gemas Azules: {gemas_azules}")
print(f"Gemas Verdes: {gemas_verdes}")
if gemas_otras > 0: 
    print(f"Gemas de Otros Colores: {gemas_otras}")
