import random
import time

def mostrar_estado(nombre, hp):
    print(f"{nombre} tiene {hp} HP restantes.")

def turno_ataque(atacante, defensor, hp_defensor):
    ataques = [
        f"{atacante} lanza un Rayo Impacto",
        f"{atacante} usa Placaje",
        f"{atacante} ataca con un Golpe Rápido",
        f"{atacante} utiliza un Ataque Especial"
    ]
    ataque_elegido = random.choice(ataques)
    daño = random.randint(5, 20)
    print(f"{ataque_elegido} y causa {daño} de daño a {defensor}!")
    hp_defensor -= daño
    if hp_defensor < 0:
        hp_defensor = 0
    time.sleep(1)
    return hp_defensor

def animacion_batalla():
    anim = ["⚡", "🔥", "💥", "✨", "⚡", "💨"]
    for simbolo in anim:
        print(simbolo, end=" ", flush=True)
        time.sleep(0.2)
    print()

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
    print(f"\nTu Pokémon: {nombre1} 🟢")
    print(f"Pokémon rival: {nombre2} 🔴\n")

    hp1 = 100
    hp2 = 100
    ronda = 1

    print(f"¡Comienza la batalla entre {nombre1} y {nombre2}!\n")
    time.sleep(1)

    while hp1 > 0 and hp2 > 0:
        print(f"\n=== Ronda {ronda} ===")
        animacion_batalla()
        hp2 = turno_ataque(nombre1, nombre2, hp2)
        mostrar_estado(nombre2, hp2)
        if hp2 == 0:
            print(f"\n🎉 ¡{nombre1} gana la batalla! 🎉")
            break

        time.sleep(1)
        animacion_batalla()
        hp1 = turno_ataque(nombre2, nombre1, hp1)
        mostrar_estado(nombre1, hp1)
        if hp1 == 0:
            print(f"\n💥 ¡{nombre2} gana la batalla! 💥")
            break

        time.sleep(1)
        ronda += 1

    print("\n¡Gracias por jugar a la Batalla Pokémon!")

batalla_pokemon()