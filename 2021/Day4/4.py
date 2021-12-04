import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np

FILE = "4.txt"
FILE_TEST = "4_test.txt"

def main_a(filename):
    data = lines(filename)
    tahane_cisla = data[0].rstrip().split(',')
    bingo = []
    b=[]
    for i in range(len(data)):
        if i > 1:
            if (i%6 == 2):
                b = []
            if (i%6 != 1):
                b.append(data[i].rstrip().split(' '))
            if (i%6 == 1):
                bingo.append(b)

    for b in range(len(bingo)):
        for i in range(len(bingo[b])):
            for j in range(len(bingo[b][i])):
                if(bingo[b][i][j] in tahane_cisla):
                    bingo[b][i][j] = tahane_cisla.index(bingo[b][i][j])
                else:
                    bingo[b][i][j] == 200
    max_suma = 0
    max_poradie = 1000
    max_cislo_index = 0
    cislo_binga = 0
    for b in range(len(bingo)):
        for i in range(len(bingo[b])):
            if (max(bingo[b][i]) < max_poradie):
                max_poradie = max(bingo[b][i])
                max_cislo = tahane_cisla[max_poradie]
                cislo_binga = b
        for i in range(len(bingo[b][0])):
            c = []
            for j in range(len(bingo[b])):
                c.append(bingo[b][j][i])
            if (max(c) < max_poradie):
                max_poradie = max(c)
                max_cislo = tahane_cisla[max_poradie]
                cislo_binga = b

    bingo_data = []
    b=[]
    for i in range(len(data)):
        if i > 1:
            if (i%6 == 2):
                b = []
            if (i%6 != 1):
                b.append(data[i].rstrip().split(' '))
            if (i%6 == 1):
                bingo_data.append(b)

    for i in range(len(bingo[cislo_binga])):
        for j in range(len(bingo[cislo_binga][i])):
            if (bingo[cislo_binga][i][j] > max_poradie):
                max_suma += int(bingo_data[cislo_binga][i][j])
    print(cislo_binga, max_poradie, max_cislo, max_suma, int(max_cislo)*int(max_suma))


def main_b(filename):
    data = lines(filename)
    tahane_cisla = data[0].rstrip().split(',')
    bingo = []
    b=[]
    for i in range(len(data)):
        if i > 1:
            if (i%6 == 2):
                b = []
            if (i%6 != 1):
                b.append(data[i].rstrip().split(' '))
            if (i%6 == 1):
                bingo.append(b)

    for b in range(len(bingo)):
        for i in range(len(bingo[b])):
            for j in range(len(bingo[b][i])):
                if(bingo[b][i][j] in tahane_cisla):
                    bingo[b][i][j] = tahane_cisla.index(bingo[b][i][j])
                else:
                    bingo[b][i][j] == 200
    max_suma = 0
    max_poradie = []
    max_cislo = []
    for b in range(len(bingo)):
        max_poradie.append(1000)
        max_cislo.append(0)
        for i in range(len(bingo[b])):
            if (max(bingo[b][i]) < max_poradie[b]):
                max_poradie[b] = max(bingo[b][i])
                max_cislo[b] = tahane_cisla[max_poradie[b]]
        for i in range(len(bingo[b][0])):
            c = []
            for j in range(len(bingo[b])):
                c.append(bingo[b][j][i])
            if (max(c) < max_poradie[b]):
                max_poradie[b] = max(c)
                max_cislo[b] = tahane_cisla[max_poradie[b]]

    poradie = max(max_poradie)
    cislo = max_cislo[max_poradie.index(poradie)]
    cislo_binga = max_poradie.index(poradie)

    bingo_data = []
    b=[]
    for i in range(len(data)):
        if i > 1:
            if (i%6 == 2):
                b = []
            if (i%6 != 1):
                b.append(data[i].rstrip().split(' '))
            if (i%6 == 1):
                bingo_data.append(b)

    for i in range(len(bingo[cislo_binga])):
        for j in range(len(bingo[cislo_binga][i])):
            if (bingo[cislo_binga][i][j] > poradie):
                max_suma += int(bingo_data[cislo_binga][i][j])
    print(cislo_binga, poradie, cislo, max_suma, int(cislo)*int(max_suma))


main_a(FILE_TEST)
main_a(FILE)
main_b(FILE_TEST)
main_b(FILE)
