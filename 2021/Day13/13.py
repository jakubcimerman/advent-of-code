import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 17
test_exp_b = 0


def main_a(filename):
    data = file(filename)
    data = data.split("\n\n")
    d = data[0].split("\n")
    instructions = data[1].split("\n")
    dots = []
    for line in d:
        x,y = line.split(",")
        dots.append([int(x),int(y)])
    inst = instructions[0].split(" ")[2].split("=")
    suma = 0
    if (inst[0] == "x"):
        for dot in dots:
            x, y = dot
            if (x > int(inst[1])):
                new_x = int(inst[1]) - (x - int(inst[1]))
                if [new_x, y] not in dots:
                    suma += 1
            else:
                suma += 1
    if (inst[0] == "y"):
        for dot in dots:
            x, y = dot
            if (y > int(inst[1])):
                new_y = int(inst[1]) - (y - int(inst[1]))
                if [x, new_y] not in dots:
                    suma += 1
            else:
                suma += 1
    return suma


def main_b(filename):
    data = file(filename)
    data = data.split("\n\n")
    d = data[0].split("\n")
    instructions = data[1].split("\n")
    dots = []
    for line in d:
        x,y = line.split(",")
        dots.append([int(x),int(y)])
    inst = instructions[0].split(" ")[2].split("=")
    for inst in instructions:
        i = inst.split(" ")[2].split("=")
        new_dots = []
        if (i[0] == "x"):
            for dot in dots:
                x, y = dot
                if (x > int(i[1])):
                    new_x = int(i[1]) - (x - int(i[1]))
                    if [new_x, y] not in dots:
                        new_dots.append([new_x, y])
                else:
                    new_dots.append([x,y])
        if (i[0] == "y"):
            for dot in dots:
                x, y = dot
                if (y > int(i[1])):
                    new_y = int(i[1]) - (y - int(i[1]))
                    if [x, new_y] not in dots:
                        new_dots.append([x, new_y])
                else:
                    new_dots.append([x,y])
        dots = new_dots.copy()
    result = ""
    for i in range(6):
        for j in range(40):
            if [j, i] in dots:
                result += "#"
            else:
                result += " "
        result += "\n"
    return result

test_and_submit(main_a, DAY, test_exp_a, "a")
print(main_b("13.txt"))