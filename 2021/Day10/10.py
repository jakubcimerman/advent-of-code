import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 26397
test_exp_b = 288957

opens = ["(", "{", "[", "<"]
closes = [")", "}", "]", ">"]


def main_a(filename):
    data = load_map_ll(filename)
    score = [3, 1197, 57, 25137]
    suma = 0
    for l in data:
        opened = []
        for i in range(len(l)):
            if l[i] in opens:
                opened.append(l[i])
            else:
                if (closes.index(l[i]) == opens.index(opened[-1])):
                    del opened[-1]
                else:
                    suma += score[closes.index(l[i])]
                    break

    return suma


def is_corrupted(l):
    opened = []
    for i in range(len(l)):
        if l[i] in opens:
            opened.append(l[i])
        else:
            if (closes.index(l[i]) == opens.index(opened[-1])):
                del opened[-1]
            else:
                return True
    return False


def main_b(filename):
    data = load_map_ll(filename)
    score = [1, 3, 2, 4]
    points = []
    for l in data:
        if (is_corrupted(l) == False):
            opened = []
            for i in range(len(l)):
                if l[i] in opens:
                    opened.append(l[i])
                else:
                    if (closes.index(l[i]) == opens.index(opened[-1])):
                        del opened[-1]
                    else:
                        print("something went wrong")
            suma = 0
            for i in range(len(opened)):
                suma = suma * 5 + score[opens.index(opened[len(opened) - i - 1])]
            points.append(suma)
    points.sort()
    return points[int((len(points)-1)/2)]

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")