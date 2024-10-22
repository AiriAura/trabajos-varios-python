def mostrar_menu():
    print("""----- Menú de opciones -----
1. Votar
2. Ver resultados   
3. Salir
""")
    return int(input("Ingrese alguna opción: "))

def votar():
    return int(input(""" Vote por un candidato:
1. Ignacio Socías
2. Lucas Espinoza  
3. Pao San Martín
"""))

def actualizar_votos(votacion_candidato, saldo_candidatos):
    
    if votacion_candidato in saldo_candidatos:
        saldo_candidatos[votacion_candidato] += 1
    

def mostrar_resultados(saldo_candidatos):
    print(f""" Votos
1. Ignacio Socías: {saldo_candidatos[1]}
2. Lucas Espinoza: {saldo_candidatos[2]}
3. Pao San Martín: {saldo_candidatos[3]}
""")

def main():
    saldo_candidatos = {1: 0, 2: 0, 3: 0}
    opcion_usuario = 0

    while opcion_usuario != 3:
        opcion_usuario = mostrar_menu()

        if opcion_usuario == 1:
            votacion_candidato = votar()
            actualizar_votos(votacion_candidato, saldo_candidatos)
        elif opcion_usuario == 2:
            mostrar_resultados(saldo_candidatos)
        elif opcion_usuario == 3:
            print("Gracias por su votación")
        else:
            print("Opción no válida, por favor elija una opción del menú.")



main()
