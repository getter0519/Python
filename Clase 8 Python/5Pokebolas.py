import random
import time

def intentar_capturar_pokemon():
    pokebolas = 5
    capturado = False
    print("¡Un Pokémon salvaje ha aparecido!")
    time.sleep(1)
    print("¡Tienes 5 Pokébolas para intentar capturarlo!")
    time.sleep(1)

    while pokebolas > 0 and not capturado:
        print(f"\nIntento con Pokébola #{6 - pokebolas}...")
        input("Presiona Enter para lanzar la Pokébola...")
        print("¡Lanzando Pokébola!")
        time.sleep(1)
        animacion = ["•", "••", "•••", "••", "•"]
        for punto in animacion:
            print(f"La Pokébola se mueve {punto}")
            time.sleep(0.4)
        exito = random.choice([True, False])
        if exito:
            print("\n¡Felicidades! ¡Has capturado el Pokémon! 🎉")
            capturado = True
        else:
            print("¡Oh no! El Pokémon se escapó de la Pokébola.")
            pokebolas -= 1
            if pokebolas > 0:
                print(f"Te quedan {pokebolas} Pokébolas.")
            time.sleep(1)

    if not capturado:
        print("\nTe has quedado sin Pokébolas. El Pokémon escapó. 😢")

intentar_capturar_pokemon()