#!/usr/bin/python
# -*- coding: utf-8 -*-

# Practicas de Desarrollo de Aplicaciones para Internet (DAI)
# Copyright (C) 2013 - 2018 - Zerjillo (zerjioi@ugr.es)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PIL import Image


def pintaMandelbrot(x1, y1, x2, y2, ancho, iteraciones, nombreFicheroPNG):
    '''
    Función que pinta en una ventana y salva en formato PNG
    el fractal de Mandelbrot.
    Nota: iteraciones tiene que ser menor que 1000
    '''
    xa = float(x1)
    xb = float(x2)
    ya = float(y1)
    yb = float(y2)
    maxIt = iteraciones
    # image size
    imgx = int(ancho)
    imgy = int(abs(yb - ya) * imgx / abs(xb - xa))

    im = Image.new('RGB', (imgx, imgy), color='black')

    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya

        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = zx + zy * 1j
            c = z

            for i in range(maxIt):
                if abs(z) > 2.0:
                    break
                z = z * z + c

            i = maxIt - i

            col = (i % 10*25, i % 16*16, i % 8*32)

            im.putpixel((x, y), col)

    im.save(nombreFicheroPNG)  # Grabamos en formato PNG


if __name__ == '__main__':
    x1 = float(input("Introduce x1: "))
    y1 = float(input("Introduce y1: "))
    x2 = float(input("Introduce x2: "))
    y2 = float(input("Introduce y2: "))

    pintaMandelbrot(x1, y1, x2, y2, 400, 255, "fich.png")
