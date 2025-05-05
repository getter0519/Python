import random
import time

def intentar_capturar_pokemon():
    pokebolas = 5
    capturado = False

    while pokebolas > 0 and not capturado:
        print(f"\nIntento con Pokébola #{6 - pokebolas}...")
        time.sleep(1)
        exito = random.choice([True, False])
        if exito:
            print("¡Felicidades! ¡Has capturado el Pokémon!")
            capturado = True
        else:
            print("El Pokémon se escapó.")
            pokebolas -= 1

    if not capturado:
        print("\nTe has quedado sin Pokébolas. El Pokémon escapó.")

intentar_capturar_pokemon()