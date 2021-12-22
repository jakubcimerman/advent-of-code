import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 590784
test_exp_b = 2758514936282235


def overlap(xmin, xmax, ymin, ymax, zmin, zmax, i):
    x = (min(xmax, i[1]) - max(xmin, i[0])) >= 0
    y = (min(ymax, i[3]) - max(ymin, i[2])) >= 0
    z = (min(zmax, i[5]) - max(zmin, i[4])) >= 0
    return x and y and z

def overlap_size(xmin, xmax, ymin, ymax, zmin, zmax, inst, i, j):
    instruction = inst[j]
    diff_x = min(xmax, instruction[1]) - max(xmin, instruction[0]) + 1
    diff_y = min(ymax, instruction[3]) - max(ymin, instruction[2]) + 1
    diff_z = min(zmax, instruction[5]) - max(zmin, instruction[4]) + 1
    total_volume = diff_x*diff_y*diff_z 
    for k in range(j):
        if overlap(max(xmin, instruction[0]), min(xmax, instruction[1]), max(ymin, instruction[2]), min(ymax, instruction[3]), max(zmin, instruction[4]), min(zmax, instruction[5]), inst[k]):
            total_volume -= overlap_size(max(xmin, instruction[0]), min(xmax, instruction[1]), max(ymin, instruction[2]), min(ymax, instruction[3]), max(zmin, instruction[4]), min(zmax, instruction[5]), inst, i, k)
    return total_volume


def main_a(filename):
    data = lines(filename)
    inst = []
    total_cubes = 0
    for line in data:
        l = line.rstrip().split(" x=")
        instruction = l[0]
        l = l[1].split(",y=")
        x_inst = l[0]
        l = l[1].split(",z=")
        y_inst = l[0]
        z_inst = l[1]
        [xmin, xmax] = x_inst.split("..")
        [ymin, ymax] = y_inst.split("..")
        [zmin, zmax] = z_inst.split("..")
        xmin = int(xmin)
        xmax = int(xmax)
        ymin = int(ymin)
        ymax = int(ymax)
        zmin = int(zmin)
        zmax = int(zmax)
        inst.append([xmin, xmax, ymin, ymax, zmin, zmax, instruction])

    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                changed = False
                #i = len(inst)-1
                i = 20
                while not changed:
                    [xmin, xmax, ymin, ymax, zmin, zmax, instruction] = inst[i]
                    if x >= xmin and x <= xmax and y >= ymin and y <= ymax and z >= zmin and z <= zmax:
                        if instruction == "on":
                            total_cubes += 1
                        changed = True
                    i -= 1
                    if i < 0:
                        changed = True

    return total_cubes



def main_b(filename):
    data = lines(filename)
    inst = []
    total_cubes = 0
    for line in data:
        l = line.rstrip().split(" x=")
        instruction = l[0]
        l = l[1].split(",y=")
        x_inst = l[0]
        l = l[1].split(",z=")
        y_inst = l[0]
        z_inst = l[1]
        [xmin, xmax] = x_inst.split("..")
        [ymin, ymax] = y_inst.split("..")
        [zmin, zmax] = z_inst.split("..")
        xmin = int(xmin)
        xmax = int(xmax)
        ymin = int(ymin)
        ymax = int(ymax)
        zmin = int(zmin)
        zmax = int(zmax)
        inst.append([xmin, xmax, ymin, ymax, zmin, zmax, instruction])

    inst = inst[::-1]

    for i in range(len(inst)):
        [xmin, xmax, ymin, ymax, zmin, zmax, instruction] = inst[i]
        if instruction == "on":
            cubes_to_add = (xmax-xmin + 1)*(ymax - ymin + 1)*(zmax - zmin + 1)
            for j in range(i):
                if overlap(xmin, xmax, ymin, ymax, zmin, zmax, inst[j]):
                    cubes_to_add -= overlap_size(xmin, xmax, ymin, ymax, zmin, zmax, inst, i, j)
            cubes_to_add = max(cubes_to_add,0)
            total_cubes += cubes_to_add

    return total_cubes

    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

