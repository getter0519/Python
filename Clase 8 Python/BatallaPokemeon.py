import random
import time

def mostrar_estado(nombre, hp):
    print(f"{nombre} tiene {hp} HP restantes.")

def turno_ataque(atacante, defensor, hp_defensor):
    daño = random.randint(5, 20)
    print(f"{atacante} ataca y causa {daño} de daño.")
    hp_defensor -= daño
    if hp_defensor < 0:
        hp_defensor = 0
    time.sleep(1)
    return hp_defensor

def batalla_pokemon():
    pokemones = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle"]
    print("Pokémon disponibles:")
    for i, poke in enumerate(pokemones, 1):
        print(f"{i}. {poke}")
    eleccion = input("Elige tu Pokémon (1-4): ").strip()
    if eleccion in ["1", "2", "3", "4"]:
        nombre1 = pokemones[int(eleccion)-1]
    else:
        print("Opción no válida. Se selecciona Pikachu por defecto.")
        nombre1 = "Pikachu"

    nombre2 = random.choice([p for p in pokemones if p != nombre1])
    print(f"Tu Pokémon: {nombre1}")
    print(f"Pokémon rival: {nombre2}\n")

    hp1 = 100
    hp2 = 100
    ronda = 1

    print(f"¡Comienza la batalla entre {nombre1} y {nombre2}!\n")
    time.sleep(1)

    while hp1 > 0 and hp2 > 0:
        print(f"\n--- Ronda {ronda} ---")
        hp2 = turno_ataque(nombre1, nombre2, hp2)
        mostrar_estado(nombre2, hp2)
        if hp2 == 0:
            print(f"\n¡{nombre1} gana la batalla!")
            break

        time.sleep(1)
        hp1 = turno_ataque(nombre2, nombre1, hp1)
        mostrar_estado(nombre1, hp1)
        if hp1 == 0:
            print(f"\n¡{nombre2} gana la batalla!")
            break

        time.sleep(1)
        ronda += 1

batalla_pokemon()