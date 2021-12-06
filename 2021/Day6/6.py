import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np

FILE = "6.txt"
FILE_TEST = "6_test.txt"

def main_a(filename):
    data = lines(filename)
    ryby = data[0].rstrip().split(',')
    for i in range(len(ryby)):
        ryby[i] = int(ryby[i])
    days = 80
    for i in range(days):
        for j in range(len(ryby)):
            if (ryby[j] == 0):
                ryby[j] = 6
                ryby.append(8)
            else:
                ryby[j] -= 1
    print(len(ryby))


def main_b(filename):
    data = lines(filename)
    ryby = data[0].rstrip().split(',')
    for i in range(len(ryby)):
        ryby[i] = int(ryby[i])
    days = 256
    """
    The code will calculate fishes at steps of 7 days, so to get 256 we 
    need to calculate first 4 days manually
    """
    days_2 = 4
    for i in range(days_2):
        for j in range(len(ryby)):
            if (ryby[j] == 0):
                ryby[j] = 6
                ryby.append(8)
            else:
                ryby[j] -= 1

    """
    The trick is that each 7 days a fish with number 3 produces a fish with 
    number 5, fish with number 4 produces a fish with number 6 and so on.
    Fishes 7 and 8 actually don't produce anything, so we have to subtract
    them from their previous count
    """
    ryby_dni = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for r in ryby:
        ryby_dni[r] += 1
    cur_date = 0
    while True:
        cur_date += 7
        ryby_dni_add = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ryby_dni_add[5] = ryby_dni[3]
        ryby_dni_add[4] = ryby_dni[2]
        ryby_dni_add[3] = ryby_dni[1]
        ryby_dni_add[2] = ryby_dni[0]
        ryby_dni_add[1] = ryby_dni[8]
        ryby_dni_add[0] = ryby_dni[7]
        ryby_dni_add[8] = ryby_dni[6] - ryby_dni[8]
        ryby_dni_add[7] = ryby_dni[5] - ryby_dni[7]
        ryby_dni_add[6] = ryby_dni[4]
        for j in range(len(ryby_dni)):
            ryby_dni[j] += ryby_dni_add[j]
        if (cur_date + 7 > days - days_2):
            break
    total = 0
    for pocet in ryby_dni:
        total += pocet
    print(total)

main_a(FILE_TEST)
main_a(FILE)
main_b(FILE_TEST)
main_b(FILE)
