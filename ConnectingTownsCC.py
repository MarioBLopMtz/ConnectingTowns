#!/bin/python3

import math
import os
import random
import re
import sys

def connectingTowns(n, routes):
    total_routes = 1
    for route in routes:
        total_routes *= route  # Multiplica el valor de la ruta actual al total de rutas
        total_routes %= 1234567  # Aplica el módulo 1234567 al total de rutas
    return total_routes  # Retorna el total de rutas

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Lee el número de casos de prueba

    for t_itr in range(t):
        n = int(input().strip())  # Lee el número de ciudades

        routes = list(map(int, input().rstrip().split()))  # Lee el arreglo de rutas entre las ciudades

        result = connectingTowns(n, routes)  # Llama a la función connectingTowns para obtener el resultado

        fptr.write(str(result) + '\n')  # Escribe el resultado en el archivo de salida

    fptr.close()  # Cierra el archivo de salida
