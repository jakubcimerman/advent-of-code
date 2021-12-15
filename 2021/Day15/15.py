import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
from collections import Counter

DAY = datetime.date.today().day
test_exp_a = 40
test_exp_b = 315


def isInsideGrid(x, y, width):
    return x >= 0 and x < width and y >= 0 and y < width


def findMinDistance(cells, distance):
    min_value = 1000000000
    min_x = 0
    min_y = 0
    for (x,y) in cells:
        if distance[x][y] < min_value:
            min_x = x
            min_y = y
            min_value = distance[x][y]
    return [min_x, min_y]


def shortest(data):
    width = len(data)
    distance = []
    for i in range(width):
        l = []
        for j in range(width):
            l.append(100000000)
        distance.append(l)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    distance[0][0] = data[0][0]

    cells = []
    cells.append([0, 0])

    while cells:


        pos = findMinDistance(cells, distance)
        cells.remove(pos)

        for i in range(4):
            x = pos[0] + dx[i]
            y = pos[1] + dy[i]

            if not isInsideGrid(x, y, width):
                continue

            if (distance[x][y] > distance[pos[0]][pos[1]] + data[x][y]):
                if [x, y] in cells:
                    cells.remove([x,y])

                distance[x][y] = distance[pos[0]][pos[1]] + data[x][y]
                cells.append([x,y])

    return distance[width - 1][width - 1] - distance[0][0]


def main_a(filename):
    data = load_map_ll(filename)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

    return shortest(data)


def main_b(filename):
    data = load_map_ll(filename)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    new_data = []
    for i in range(5):
        for x in range(len(data)):
            line = []
            for j in range(5):
                for y in range(len(data)):
                    nd = (data[x][y] + j + i - 1) % 9 + 1
                    line.append(nd)

            new_data.append(line)

    return shortest(new_data)
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")
