import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 15
test_exp_b = 1134

def data_borders(data):
    result = []
    for i in range(len(data)+2):
        line = []
        for j in range(len(data[0])+2):
            if (j == 0 or i == 0 or i == len(data)+1 or j == len(data[0])+1):
                line.append(9)
            else:
                line.append(data[i-1][j-1])
        result.append(line)
    return result

def main_a(filename):
    data = load_map_ll(filename)
    suma = 0
    max_i = len(data)
    max_j = len(data[0])
    for i in range(max_i):
        for j in range(max_j):
            data[i][j] = int(data[i][j])
    data = data_borders(data)
    for ir in range(max_i):
        for jr in range(max_j):
            i = ir + 1
            j = jr + 1
            if(data[i][j] < data[i+1][j] and data[i][j] < data[i][j+1] and data[i][j] < data[i-1][j] and data[i][j] < data[i][j-1]):
                suma += data[i][j] + 1
    return suma

def check_neighbours(data, ir, jr):
    i = ir
    j = jr
    higher_neighbours = []
    if(data[i][j] == 8):
        return []
    if(data[i][j] < data[i+1][j] and data[i+1][j] < 9):
        higher_neighbours.append([i+1, j])
    if(data[i][j] < data[i-1][j] and data[i-1][j] < 9):
        higher_neighbours.append([i-1, j])
    if(data[i][j] < data[i][j+1] and data[i][j+1] < 9):
        higher_neighbours.append([i, j+1])
    if(data[i][j] < data[i][j-1] and data[i][j-1] < 9):
        higher_neighbours.append([i, j-1])
    return higher_neighbours


def main_b(filename):
    data = load_map_ll(filename)
    suma = 0
    max_i = len(data)
    max_j = len(data[0])
    low_points = []
    for i in range(max_i):
        for j in range(max_j):
            data[i][j] = int(data[i][j])
    data = data_borders(data)
    for ir in range(max_i):
        for jr in range(max_j):
            i = ir + 1
            j = jr + 1
            if(data[i][j] < data[i+1][j] and data[i][j] < data[i][j+1] and data[i][j] < data[i-1][j] and data[i][j] < data[i][j-1]):
                low_points.append([i, j])
    
    sizes = []
    for lp in low_points:
        basin = []
        basin.append(lp)
        smthng_changed = True
        while smthng_changed:
            smthng_changed = False
            for b in basin:
                i = b[0]
                j = b[1]
                new_neighbours = check_neighbours(data,i,j)
                for nb in new_neighbours:
                    if nb not in basin:
                        basin.append(nb)
                        smthng_changed = True
        sizes.append(len(basin))
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")