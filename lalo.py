import random
import time
from IPython.display import clear_output

# Lista de preguntas#
preguntas = [
    {
        "pregunta": "¿Cuál es el símbolo químico del carbono?",
        "respuestas": ["C", "O", "H", "N"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Cuál es el número atómico del oxígeno?",
        "respuestas": ["8", "6", "7", "9"],
        "respuesta_correcta": "8"
    },
    {
        "pregunta": "¿Cuál es el símbolo químico del hierro?",
        "respuestas": ["Fe", "He", "Hg", "Ag"],
        "respuesta_correcta": "Fe"
    },
    {
        "pregunta": "¿Cuál es el número atómico del nitrógeno?",
        "respuestas": ["7", "6", "8", "9"],
        "respuesta_correcta": "7"
    },
    {
        "pregunta": "¿Cuál es el símbolo químico del sodio?",
        "respuestas": ["Na", "K", "Ca", "Mg"],
        "respuesta_correcta": "Na"
    }
]

# Reglas del juegitoooo#
def explicar_reglas():
    print("Bienvenido al juego de preguntas y respuestas de quimica analitica.")
    print("El objetivo del juego es responder correctamente el mayor número de preguntas posible antes de perder todas tus vidas.")
    print("Por cada respuesta correcta, ganarás 20 puntos de vida.")
    print("Por cada respuesta incorrecta, perderás 20 puntos de vida.")
    print("Tienes un total de 100 puntos de vida no creo que pierdas.")
    print("Si pierdes todas tus vidas, el juego termina y te dira una frase motivadora")
    print("¡Buena suerte!")
    print("Ademas el juego te insultara de vez en cuando asi que no te preocupes no lo dice encerio o si?")
# Mostrador de preguntas#
def mostrar_pregunta(pregunta, respuestas):
    print(pregunta)
    for i in range(len(respuestas)):
        print(str(i + 1) + ": " + respuestas[i])
    print()

# Función para mostrar la barra de vida#
def mostrar_vida(vida):
    print("Vida:", end="")
    for i in range(vida):
        print("■", end="")
    print()

# Función para mostrar el texto de la respuesta#
def mostrar_respuesta(respuesta):
    print("Respuesta:", respuesta)

# Función para mostrar la muerte#
def mostrar_game_over():
    print("Contaduria tiene buena demanda")

# quitador de preguntas#
def limpiar_salida():
    clear_output(wait=True)

# iniciador del juego#
def jugar_juego():
    explicar_reglas()
    # vida del jugador#
    vida_actual = 100

    # pregunta aleatoria#
    pregunta_actual = random.choice(preguntas)

    # Corazon del juego#

    while True:
        # Limpiar la salida mostrar pregunta y vida
        limpiar_salida()
        mostrar_pregunta(pregunta_actual["pregunta"], pregunta_actual["respuestas"])
        mostrar_vida(vida_actual)
        # Esperar respuesta del jugador#
        respuesta_jugador = input("Respuesta: ")

        # Comprobar si la respuesta es correcta ademas del intercambiador de si la riega#
        if respuesta_jugador == pregunta_actual["respuesta_correcta"]:
            mostrar_respuesta("Correcto!")
            mostrar_respuesta("mmmmmmmmmmmmmmmmmm")
            time.sleep(1)
            if vida_actual > 100:
                vida_actual = 100
            pregunta_actual = random.choice(preguntas)
        else:
            mostrar_respuesta("JAJJAJAJAJAJAJAJAJAJAJA!")
            time.sleep(1)
            vida_actual -= 20
            if vida_actual <= 0:
                limpiar_salida()
                mostrar_game_over()
                return
            else:
                mostrar_respuesta("A ESTUDIAAAARRRRRRR")
                time.sleep(2)
                pregunta_actual = random.choice(preguntas)
                continue
jugar_juego()
