import sys
sys.path.insert(0,'..')
from aoc import *

FILE = "2.txt"
FILE_TEST = "2_test.txt"

def main_a(filename):
    pocet = 0
    x = 0
    d = 0
    a = 0
    data = load_strings_split(filename, " ")
    for line in data:
        smer = line[0]
        krok = int(line[1])
        if (smer[0] == "f"):
            x += krok
        if (smer[0] == "u"):
            d -= krok
        if (smer[0] == "d"):
            d += krok
    print(x*d)

def main_b(filename):
    pocet = 0
    x = 0
    d = 0
    a = 0
    data = load_strings_split(filename, " ")
    for line in data:
        smer = line[0]
        krok = int(line[1])
        if (smer[0] == "f"):
            x += krok
            d += a*krok
        if (smer[0] == "u"):
            a -= krok
        if (smer[0] == "d"):
            a += krok
    print(x*d)

main_a(FILE_TEST)
main_a(FILE)
main_b(FILE_TEST)
main_b(FILE)