import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
from collections import Counter
import math

DAY = datetime.date.today().day
test_exp_a = 45
test_exp_b = 112


def balistic(xmin, xmax, ymin, ymax):
    """
    Limits for initial velocity:
    - vxmin - solution of equation vxmin*(vxmin+1)/2 = xmin 
    - vxmax - the probe cannot be more far away then xmax after one step
    - vymin - the probe cannot be deeper then ymin after one step
    - vymax - we know from physics, that when the probe is falling down, then at y = 0 it has
              the same velocity with the opposite sign and then it cannot do step bigger then
              -ymin
    """
    vxmin = int((-1 + math.sqrt(1+4*2*xmin)) / 2)
    vxmax = xmax
    vymin = ymin
    vymax = -ymin

    max_height = 0
    pocet = 0
    for i in range(vxmin - 1 ,vxmax + 1):
        for j in range(vymin - 1, vymax + 1):
            vx = i
            vy = j
            x = 0
            y = 0

            max_height_in_run = 0
            hit = False
            while x <= xmax and y >= ymin and not hit:
                x += vx
                y += vy
                if (vx > 0):
                    vx -= 1
                vy -= 1
                if y > max_height_in_run:
                    max_height_in_run = y

                if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
                    hit = True
                    pocet += 1
                    if max_height_in_run > max_height:
                        max_height = max_height_in_run
    return [max_height, pocet]



def main_a(filename):
    data = file(filename)
    data = data.split(" x=")[1].split(", y=")
    xmin, xmax = data[0].split("..")
    ymin, ymax = data[1].split("..")
    xmin = int(xmin)
    xmax = int(xmax)
    ymin = int(ymin)
    ymax = int(ymax)

    height, pocet = balistic(xmin, xmax, ymin, ymax)
    return height


def main_b(filename):
    data = file(filename)
    data = data.split(" x=")[1].split(", y=")
    xmin, xmax = data[0].split("..")
    ymin, ymax = data[1].split("..")
    xmin = int(xmin)
    xmax = int(xmax)
    ymin = int(ymin)
    ymax = int(ymax)

    vxmin = int((-1 + math.sqrt(1+4*2*xmin)) / 2)

    height, pocet = balistic(xmin, xmax, ymin, ymax)
    return pocet
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")
