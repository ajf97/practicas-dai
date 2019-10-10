# -*- coding: utf-8 -*-
# @title: Ejercicio 4: Sucesión de Fibonnacci
# @author: Alejandro Jerónimo Fuentes
# @date: 23/09/2019
#

import math


def fibonnacci(number):
    if number < 2:
        return number
    else:
        return fibonnacci(number - 1) + fibonnacci(number - 2)


filename = input('Introduce el nombre del archivo: ')
input_file = open(filename, 'r')

number = int(input_file.read())
input_file.close()

fibonnacci_element = fibonnacci(number)

output_file = open('salida_fibonnacci.txt', 'w')
output_file.write(str(fibonnacci_element))
output_file.close()
