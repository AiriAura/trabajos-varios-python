opcion_usuario = 0


while opcion_usuario !=3:

    print("""----- Horóscopo Python-----
    1. Saber mi Horóscopo
    2. Saber mi Signo Zodiacal
    3. Salir
    """)

    opcion_usuario = int(input("Ingrese alguna opción: "))

    if(opcion_usuario == 1):
        horoscopo_usuario = int(input("""" Para saber tu horóscopo, elige el número con tu signo zodiacal:
        1. ARIES
        2. TAURO 
        3. GÉMINIS
        4. CÁNCER
        5. LEO
        6. VIRGO
        7. LIBRA
        8. ESCORPIO
        9. SAGITARIO
        10. CAPRICORNIO
        11. ACUARIO
        12. PISCIS                                                                                                                                                                                  
        """))
        

        horoscopo  = {
               
              1: " tendrás una buena noticia esta semana",
              2: "usa colores vivos, ",
              3: "usa colores vivos, tendrás una buena noticia esta semana",
              4: "usa colores vivos esta semana",
              5:"sonríe más",
              6: "tendrás éxito",
              7: "usa colores vivos, tendrás una buena noticia esta semana",
              8: "tendrás una buena noticia esta semana",
              9: "usa colores vivos, tendrás una buena noticia esta semana",
              10:"usa colores vivos, tendrás una buena noticia esta semana",
              11:"usa colores vivos, tendrás una buena noticia esta semana",
              12: "usa colores vivos, tendrás una buena noticia esta semana"
        
        }
        if horoscopo_usuario in horoscopo:
            print(horoscopo[horoscopo_usuario])
        else:
            print("Ingresa una opción válida")        

        


    if (opcion_usuario ==2):
        dia = int(input("Para saber tu signo, ingresa tu día de nacimiento: "))
        mes = input ("Ahora ingresa tu mes en palabras: ").lower().strip()
            
 

        from signos import signos_zodiacales

        for signo in signos_zodiacales:

            if dia >= signos_zodiacales[signo]["desde"]["día"] and mes == signos_zodiacales[signo]["desde"]["mes"] or dia <= signos_zodiacales[signo]["hasta"]["día"] and mes == signos_zodiacales[signo]["hasta"]["mes"]:
                print(signo)





    if opcion_usuario == 3:
        exit
        print("Gracias por utilizar el horóscopo") 
                