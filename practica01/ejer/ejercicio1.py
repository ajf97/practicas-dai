# -*- coding: utf-8 -*-
# @title: Ejercicio 1: Adivina un número
# @author: Alejandro Jerónimo Fuentes
# @date: 20/09/2019
#

import random

MAX_ATTEMPTS = 10
RANDOM_NUMBER = random.randint(1, 100)

print('Bienvenido a ADIVINA UN NÚMERO (entre 1 y 100)')

for attempt in range(MAX_ATTEMPTS):
    print(f"Te quedan {MAX_ATTEMPTS-attempt} intentos")
    number = int(input('Introduce el número: '))

    if (attempt == MAX_ATTEMPTS-1):
        print('Se te han agotado todos los intentos')
        break

    if (number < RANDOM_NUMBER):
        print('El número buscado es mayor')
    elif (number > RANDOM_NUMBER):
        print('El número buscado es menor')
    else:
        print('¡Has acertado!')
        break
