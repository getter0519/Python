def resultado_combate(poder_ataque, poder_defensa):
    if poder_ataque > poder_defensa:
        return "¡Ganaste el combate!"
    elif poder_ataque < poder_defensa:
        return "¡Perdiste el combate!"
    else:
        return "¡El combate terminó en empate!"
    
poder_ataque = int(input("Ingresa el poder de ataque del jugador: "))
poder_defensa = int(input("Ingresa el poder de defensa del enemigo: "))

resultado = resultado_combate(poder_ataque, poder_defensa)
print(resultado)