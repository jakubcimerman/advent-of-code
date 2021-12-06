import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np

FILE = "6.txt"
FILE_TEST = "6_test.txt"

def main(filename, days):
    data = lines(filename)
    r = data[0].rstrip().split(',')
    ryby = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(r)):
        ryby[int(r[i])] += 1 

    for i in range(days):
        new_ryby = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(len(ryby)):
            new_ryby[j] = ryby[(j+1)%9]
        new_ryby[6] += ryby[0]
        for j in range(len(ryby)):
            ryby[j] = new_ryby[j]

    total = 0
    for pocet in ryby:
        total += pocet
    print(total)


main(FILE_TEST, 80)
main(FILE, 80)
main(FILE_TEST, 256)
main(FILE, 256)
