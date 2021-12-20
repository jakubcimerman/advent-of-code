import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
from collections import Counter
import math

DAY = datetime.date.today().day
test_exp_a = 35
test_exp_b = 3351


def print_map(mapa):
    s = ""
    for i in range(len(mapa)): 
        for j in range(len(mapa[i])):
            s += mapa[i][j]
        s += "\n"
    print(s)

def count_lights(mapa):
    c = 0
    for i in range(len(mapa)): 
        for j in range(len(mapa[i])):
            c += mapa[i][j] == "#"
    return c


def main_a(filename, steps):
    data = load_block(filename)
    algorithm = data[0]
    """
    if 0-th component of algorithm is #, this means that each empty cell in the infinite image will be turned on,
    and if the last component is ., then it will be again turned off. Thus the image will be flickering
    """
    flickering = algorithm[0] == "#" and algorithm[-1] == "."
    mapa = list(map(lambda x: list(x.rstrip()), data[1].rstrip().split("\n")))
    for s in range(steps):
        if flickering:
            if (s%2 == 0):
                mapa = add_array_border(mapa, ".")
                mapa = add_array_border(mapa, ".")
            else:
                mapa = add_array_border(mapa, "#")
                mapa = add_array_border(mapa, "#")
        else:
            mapa = add_array_border(mapa, ".")
            mapa = add_array_border(mapa, ".")
        new_map = []
        for ir in range(len(mapa) - 2):
            i = ir + 1
            new_line = []
            for jr in range(len(mapa[i]) - 2):
                j = jr + 1
                binar_string = ""
                for k in range(3):
                    for l in range(3):
                        c = mapa[i + k - 1][j + l - 1]
                        if c == ".":
                            binar_string += "0"
                        else:
                            binar_string += "1"
                num = int(convert_base(binar_string, 2, 10))
                new_line.append(algorithm[num])
            new_map.append(new_line)
        mapa = new_map.copy()
    #print_map(mapa)
    return count_lights(mapa)

def main_b(filename):
    return "TBA"
    

#test_and_submit(main_a, DAY, test_exp_a, "a")
#test_and_submit(main_b, DAY, test_exp_b, "b")

print(main_a("20_test.txt", 2))
print(main_a("20.txt", 2))
print(main_a("20_test.txt", 50))
print(main_a("20.txt", 50))
