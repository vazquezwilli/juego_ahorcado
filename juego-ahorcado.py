from operator import truediv
import random


def obtener_palabras_secreta() -> str:
    palabras = ['java','php','angular','react','flask','typescript']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra  in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "*"
    
    return adivinado

def juego_ahorcado_funcion():
    palabra_secreta = obtener_palabras_secreta()
    letras_adivinadas = []
    intentos = 5
    juego_terminado = False

    print("Bienvenido al juego del ahorcado")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta,letras_adivinadas),"La cantidad de letras  de la palabra es:", len(palabra_secreta))

    while not juego_terminado  and intentos > 0:
        adivinanza = input("introduce una letra ").lower()
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("introduzca una letra valida (solo una letra)")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra intenta otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Muy bien has acertado, la letra '{adivinanza}' esta presente en la palabra secreta")
            else:
                intentos -= 1
                print(f"Lo siento la letra '{adivinanza}' no esta presente en la palabra secreta")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "*" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"Felicitaciones has ganado, La palabra completa es: '{palabra_secreta}'")
    if intentos  == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Lo sentimos te has acabado los intentos, la palabra secreta era '{palabra_secreta}'")

juego_ahorcado_funcion()
            





