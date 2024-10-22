opcion_usuario = 0
saldo_candidato1 = 0
saldo_candidato2 = 0
saldo_candidato3 = 0
votacion_candidato = 0


while opcion_usuario != 3:

    print("""----- Menú de opciones -----
1. Votar
2. Ver resultados   
3. Salir
""")

    opcion_usuario = int(input("Ingrese alguna opción: "))

    if(opcion_usuario == 1):
        votacion_candidato = int(input(""" Vote por un candidato:
1. Ignacio Socías
2. Lucas Espinoza  
3. Pao San Martín
""")
)
        if(votacion_candidato == 1):
            saldo_candidato1 = saldo_candidato1 +1
        if(votacion_candidato == 2):
            saldo_candidato2 = saldo_candidato2 +1
        if(votacion_candidato == 3):
            saldo_candidato3 = saldo_candidato3 +1




    if(opcion_usuario == 2):
        print(f""" Votos
1. Ignacio Socías: {saldo_candidato1}
2. Lucas Espinoza: {saldo_candidato2}
3. Pao San Martín: {saldo_candidato3}
""")
        
      
    if(opcion_usuario ==3):
        exit
        print("Gracias por su votación")