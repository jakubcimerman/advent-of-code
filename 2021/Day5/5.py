import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np

FILE = "5.txt"
FILE_TEST = "5_test.txt"

def main_a(filename, length):
    data = lines(filename)
    grid = []
    for i in range(length):
        grid_line = []
        for j in range(length):
            grid_line.append(0)
        grid.append(grid_line)
    for l in data:
        points = l.split(" -> ")
        x1, y1 = points[0].split(",")
        x2, y2 = points[1].rstrip().split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if (x1 == x2):
            for i in range(abs(y2-y1)+1):
                grid[y1 + np.sign(y2-y1) * i][x1] += 1
        if (y1 == y2):
            for i in range(abs(x2-x1)+1):
                grid[y1][x1 + np.sign(x2-x1) * i] += 1
    cross = 0
    for l in grid:
        for el in l:
            if el > 1:
                cross += 1
    print(cross)

def main_b(filename, length):
    data = lines(filename)
    grid = []
    for i in range(length):
        grid_line = []
        for j in range(length):
            grid_line.append(0)
        grid.append(grid_line)
    for l in data:
        points = l.split(" -> ")
        x1, y1 = points[0].split(",")
        x2, y2 = points[1].rstrip().split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if (x1 == x2):
            for i in range(abs(y2-y1)+1):
                grid[y1 + np.sign(y2-y1) * i][x1] += 1
        if (y1 == y2):
            for i in range(abs(x2-x1)+1):
                grid[y1][x1 + np.sign(x2-x1) * i] += 1
        if (abs(y1-y2) == abs(x1-x2)):
            for i in range(abs(x1-x2)+1):
                grid[y1 + np.sign(y2-y1) * i][x1 + np.sign(x2-x1) * i] += 1
    cross = 0
    for l in grid:
        for el in l:
            if el > 1:
                cross += 1
    print(cross)

main_a(FILE_TEST, 10)
main_a(FILE, 1000)
main_b(FILE_TEST, 10)
main_b(FILE, 1000)
