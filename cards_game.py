# Juego de las cartas con menú de opciones
# Sacar 2 cartas, segun lo que salga en ese par, darle premios al usuario

# Objetivos:
# Abrir visual Code, crear un archivo llamado "cards_game.py"
# Vamos a:
# - Repasar conceptos básicos de Python
# - Revisar las funciones basicas y las importadas
# - Recordar las "recetas" para los problemas más comunes
# - Analizar los nuevos requerimientos que pueden surgir una vez que ya estamos programando

# textos y numeros
# para que hacemos este programa. la idea es guardar información en estas "cajitas"
# si vamos a usar valores que sean textos, y luego necesitaremos usarlos como referencia a las preguntas
# del programa, SIEMPRE usar minuscula ó mayúscula
# Los nombres de las variables deben ser LO MAS REPRESENTATIVO POSIBLE para así sea MUCHO mas facil
# indentificar su valores cuando los necesite en el programa
# No olvidar que: Los nombres de las variables NO SIGUEN REGLAR ORTOGRAFICAS, los valores, en el caso que sean textos SI (no obligatorio)
import random

# FUNCIONES
# las funciones sirven para abstraer a los programadores de los calculos simples o complejos que se necesitan
# hacer 
# re utilizar codigo, esto quiere decir que podemos usar las mismas funciones en muchos programas distintos
def elegir_carta_al_azar():
  # random.choice nos pide que la pasemos una lista, para asi poder elegir un valor al azar entre esa list
  lista_opciones = ["as", "pica", "corazon", "trebol"]
  carta = random.choice(lista_opciones)
  # Y AHORA QUE YA HICE LOS CALCULOS EN LA FUNCIÓN ¿CÓMO ENTREGO EL RESULTADO?
  # usando la palabra return
  return carta

# Al crear una función, nos cuestinaremos lo siguiente:
# PARA HACER SU TRABAJO, LA FUNCION REQUERIRA VALORES DE VARIABLES PARA PODER HACER SU TRABAJO
# Si la respuesta es SI, entonces al crear la funcion, en los parentesis debemos definir esas variables
# IMPORTANTE!!! las variables que va a usar la función NO LLEVAN signo igual
# EL ORDEN DE ESTAS VARIABLES ES CRITICO!!!
def dibujar_tabla(wins, fails):
  print(f"""
      --------------------------
      | GANADAS    |    {wins} 
      | PERDIDAS   |    {fails}        
      --------------------------
  """)

# Para que el while ejecute MUCHAS VECES un mismo trozo de código.
# Necesitamos proveer de una pregunta al while, de manera de que de la posibilidad de terminar alguna vez 
# de ejecutar el código, de lo contrario se ejecutará INFINITAS VECES
# receta para escribir un while "PARA MENU DE OPCIONES"
# paso 1: definir la variable a la cual el usuario ingresará su opcion
# paso 2: definir si el valor solicitado el usuario será numerico o texto
# paso 3: receta -> crear la variable con un valor "vacio", incluir la variable en la pregunta el while.
# el valor vacio de los textos es "" y el valor vacio de los numeros es 0
# paso 4: dentro del while solicitar la opción al usuario
# paso 5: una vez la variable incluida en la pregunta del While, PENSAR EN QUE VALOR REPRESENTA la opcion
# que se le dio al usuario para salir. 
# Por ejemplo: la palabra "salir", la letra "N" ... el número 3 <-- significa salir 
# paso 6: en la pregunta del while usar lo siguiente:
# variable_de_la_opcion_usuario != "valor_que_elegi_como_salir"

opcion_usuario = ""
cantidad_exitos = 0
cantidad_fallos = 0

# refactorización: vuelve a mirar el codigo y mejoralo

while (opcion_usuario != "3") :
  opcion_usuario = input("dime tu opcion: 1) jugar 2) resultados 3)salir  :")

  # Entender y analizar la decision del usuario
  if (opcion_usuario == "1"):
    carta_as = "as"
    carta_pica = "pica"
    carta_corazon = "corazon"
    carta_trebol = "trebol"

    # SIEMPRE QUE UNA FUNCIÓN ME ENTREGUE UN RESULTADO, la función debe asociarse a un variable
    carta1_usuario = elegir_carta_al_azar()
    carta2_usuario = elegir_carta_al_azar()

    # no olvidar agregar la f SIEMPRE Y CUANDO el print quiera mostrar valores de variables, sino, no es necesario
    # funciones que no procesan ni entregan resultados
    print(f"""
      CARTA 1: {carta1_usuario}
      CARTA 2: {carta2_usuario}
    """)

    if (carta1_usuario == "as" and carta2_usuario == "as"):
      print("ganaste el premio máximo")
      # formula de incremento
      # 1. definir que variable va a incrementar su valor, (conteo)
      # 2. nombre_variable = nombre_variable + incremento
      #             ó
      #    nombre_variable += incremento 
      # ejemplos 
      # contador += 1 <<<-- la variable "contador" se incrementa en 1
      cantidad_exitos += 1

    elif (carta1_usuario == "corazon" and carta2_usuario == "corazon" ):
      print("ganaste el premio máximo")
      cantidad_exitos += 1
    elif (carta1_usuario == "as" and carta2_usuario == "corazon"):
      print("ganaste el premio intermedio")
      cantidad_exitos += 1
    else:
      print("lo siento, no ganaste nada. Sigue intentando")
      cantidad_fallos += 1
  if (opcion_usuario == "2"):
    # Vamos a contar cuantas veces ha ganado y cuantas a perdido. 
    # En esta opción vamos a mostrar una tabla con los resultados
    # Para contar, en programación usamos variable y la formula de incremento.
    
    # Usamos funciones para recordar el PORQUE creamos cierto código y de esta forma 
    # poder mantener un mismo código durante el tiempo y así tener más claridad
    # sobre las decisiones de programación que se tomaron en su momento
    dibujar_tabla(cantidad_exitos, cantidad_fallos)