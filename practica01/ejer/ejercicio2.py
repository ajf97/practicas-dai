# -*- coding: utf-8 -*-
# @title: Ejercicio 2: Ordenación
# @author: Alejandro Jerónimo Fuentes
# @date: 20/09/2019
#

import time
import random


def insertion(list):
    for i in range(1, len(list)):
        tmp = list[i]
        k = i

        while k > 0 and tmp < list[k - 1]:
            list[k] = list[k - 1]
            k -= 1

        list[k] = tmp


def selection(list):
    for i in range(len(list)):
        minimum = min(list[i:])
        minimum_index = list[i:].index(minimum)
        list[i + minimum_index] = list[i]
        list[i] = minimum


def generateRandomList(start, stop, number_elements):
    return [random.randint(start, stop) for i in range(number_elements)]


random_list = generateRandomList(1, 100, 10)
other_random_list = generateRandomList(1, 100, 10)


print('Lista de inserción: ', random_list)
print('Lista de selección: ', other_random_list)


starting_point = time.time()
insertion(random_list)
time_insertion = int(time.time() - starting_point)


starting_point = time.time()
selection(other_random_list)
time_selection = int(time.time() - starting_point)


print('Lista ordenada de inserción: ', random_list)
print('Lista ordenada de selección: ', other_random_list)


if (time_insertion < time_selection):
    print('El algoritmo de inserción es más rápido.')
else:
    print('El algoritmo de selección es más rápido')
