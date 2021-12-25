import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 58

def main_a(filename):
    data = load_map_ll(filename)
    step = 0
    canMove = True
    while canMove:
        canMove = False
        step += 1
        print("step", step)
        list_of_moving = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == ">":
                    if data[i][(j+1)%len(data[i])] == ".":
                        list_of_moving.append([i,j])
                        canMove = True
        for moving in list_of_moving:
            i,j = moving
            data[i][j] = "."
            data[i][(j+1)%len(data[i])] = ">"
        list_of_moving = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "v":
                    if data[(i+1)%len(data)][j] == ".":
                        list_of_moving.append([i,j])
                        canMove = True
        for moving in list_of_moving:
            i,j = moving
            data[i][j] = "."
            data[(i+1)%len(data)][j] = "v"
        print(data)
    return step
    

test_and_submit(main_a, DAY, test_exp_a, "a")