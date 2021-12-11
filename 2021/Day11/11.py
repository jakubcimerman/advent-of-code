import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 1656
test_exp_b = 195



def main_a(filename):
    steps = 100
    data = load_map_ll(filename)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    data = add_array_border(data, "X")
    flashes = 0
    for step in range(steps):
        for ir in range(len(data)-2):
            for jr in range(len(data)-2):
                i = ir + 1
                j = jr + 1
                data[i][j] += 1
        changed = True
        while changed:
            changed = False
            for ir in range(len(data)-2):
                for jr in range(len(data)-2):
                    i = ir + 1
                    j = jr + 1
                    if (data[i][j] > 9):
                        changed = True
                        flashes += 1
                        for ik in range(3):
                            for jk in range(3):
                                if (data[i+ik-1][j+jk-1] != "X" and data[i+ik-1][j+jk-1] != 0):
                                    data[i+ik-1][j+jk-1] += 1
                        data[i][j] = 0

    return flashes


def main_b(filename):
    steps = 1000
    data = load_map_ll(filename)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    data = add_array_border(data, "X")
    
    for step in range(steps):
        flashes_in_step = 0
        for ir in range(len(data)-2):
            for jr in range(len(data)-2):
                i = ir + 1
                j = jr + 1
                data[i][j] += 1
        changed = True
        while changed:
            changed = False
            for ir in range(len(data)-2):
                for jr in range(len(data)-2):
                    i = ir + 1
                    j = jr + 1
                    if (data[i][j] > 9):
                        changed = True
                        flashes_in_step += 1
                        for ik in range(3):
                            for jk in range(3):
                                if (data[i+ik-1][j+jk-1] != "X" and data[i+ik-1][j+jk-1] != 0):
                                    data[i+ik-1][j+jk-1] += 1
                        data[i][j] = 0
        if (flashes_in_step == (len(data)-2)*(len(data[0])-2)):
            return step + 1

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

