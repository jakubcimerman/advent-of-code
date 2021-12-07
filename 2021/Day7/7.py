import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np

FILE = "7.txt"
FILE_TEST = "7_test.txt"

def main_a(filename):
    data = lines(filename)
    r = data[0].rstrip().split(',')
    for i in range(len(r)):
        r[i] = int(r[i])
    best_sum = 1000000
    for i in range(max(r)-min(r)):
        j = i + min(r)
        suma = 0
        for k in range(len(r)):
            suma += abs(r[k]-j)
        if (suma < best_sum):
            best_sum = suma
    print(best_sum)

def main_b(filename):
    data = lines(filename)
    r = data[0].rstrip().split(',')
    for i in range(len(r)):
        r[i] = int(r[i])
    best_sum = 1000000000
    for i in range(max(r)-min(r)):
        j = i + min(r)
        suma = 0
        for k in range(len(r)):
            suma += abs(r[k]-j)*(abs(r[k]-j)+1)/2
        if (suma < best_sum):
            best_sum = suma
    print(best_sum)

main_a(FILE_TEST)
main_a(FILE)
main_b(FILE_TEST)
main_b(FILE)
