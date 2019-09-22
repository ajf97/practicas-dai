# -*- coding: utf-8 -*-
# @title: Ejercicio 3: La criba de Eratóstenes
# @author: Alejandro Jerónimo Fuentes
# @date: 21/09/2019
#


def cribaErastotenes(list):
    i = 0
    marked_number = list[i]
    last_number = list[-1]

    while marked_number**2 < last_number:
        for number in list[list.index(marked_number)+1:]:
            if number % marked_number == 0:
                list.pop(list.index(number))

        i += 1
        marked_number = list[i]


number = int(input('Introduce un número: '))
number_list = list(range(2, number+1))
print('Lista de números', number_list)

cribaErastotenes(number_list)

print('Números primos', number_list)
