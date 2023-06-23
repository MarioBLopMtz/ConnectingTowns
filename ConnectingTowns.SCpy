#!/bin/python3

import math
import os
import random
import re
import sys

def connectingTowns(n, routes):
    total_routes = 1
    for route in routes:
        total_routes *= route
        total_routes %= 1234567
    return total_routes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
