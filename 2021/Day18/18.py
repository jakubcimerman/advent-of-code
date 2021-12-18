import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
from collections import Counter
import math
import copy

DAY = datetime.date.today().day
test_exp_a = 4140
test_exp_b = 3993


class Pair:
    def __init__(self, x, y):
        # if (x == None):
        #     x = 0
        # if (y == None):
        #     y = 0
        self.x = x
        self.y = y

    def magnitude(self):
        x = self.x
        y = self.y
        mag_x = 0
        mag_y = 0
        if isinstance(x, Pair):
            mag_x = x.magnitude()
        else:
            mag_x = x
        if isinstance(y, Pair):
            mag_y = y.magnitude()
        else:
            mag_y = y
        return 3*mag_x + 2*mag_y

    def print(self):
        x = self.x
        y = self.y
        s = "["
        if isinstance(x, Pair):
            s += x.print()
        else:
            s += str(x)
        s += ","
        if isinstance(y, Pair):
            s += y.print()
        else:
            s += str(y)
        s += "]"
        return s

    def returnDepth(self):
        md = 1
        x = self.x
        y = self.y
        if isinstance(x, Pair):
            if x.returnDepth() + 1 > md:
                md = x.returnDepth() + 1
        if isinstance(y, Pair):
            if y.returnDepth() + 1 > md:
                md = y.returnDepth() + 1
        return md

    def returnX(self):
        return self.x

    def returnY(self):
        return self.y

    def replaceX(self, x):
        self.x = x

    def replaceY(self, y):
        self.y = y

    def containsLarge(self):
        x = self.x
        y = self.y
        if isinstance(x, Pair):
            if x.containsLarge():
                return True
        else:
            if x > 9:
                return True
        if isinstance(y, Pair):
            if y.containsLarge():
                return True
        else:
            if y > 9:
                return True
        return False

    def addValueToRight(self, value):
        x = self.x
        y = self.y
        if isinstance(x, Pair):
            done = x.addValueToRight(value)
            if done:
                return True
        else:
            self.replaceX(x + value)
            return True
        if isinstance(y, Pair):
            done = y.addValueToRight(value)
            if done:
                return True
        else:
            self.replaceY(y + value)
            return True
        return False

    def addValueToLeft(self, value):
        x = self.x
        y = self.y
        if isinstance(y, Pair):
            done = y.addValueToLeft(value)
            if done:
                return True
        else:
            self.replaceY(y + value)
            return True
        if isinstance(x, Pair):
            done = x.addValueToLeft(value)
            if done:
                return True
        else:
            self.replaceX(x + value)
            return True
        return False


def explode(p):
    fromLeft = 0
    fromRight = 0
    if isinstance(p.returnX(), Pair) and p.returnX().returnDepth() == 4:
        p1 = p.returnX()
        p1x = 0
        fromRight += 1
    else:
        p1 = p.returnY()
        p1x = 1
        fromLeft += 1
    if isinstance(p1.returnX(), Pair) and p1.returnX().returnDepth() == 3:
        p2 = p1.returnX()
        p2x = 0
        fromRight += 1
    else:
        p2 = p1.returnY()
        p2x = 1
        fromLeft += 1
    if isinstance(p2.returnX(), Pair) and p2.returnX().returnDepth() == 2:
        p3 = p2.returnX()
        p3x = 0
        fromRight += 1
    else:
        p3 = p2.returnY()
        p3x = 1
        fromLeft += 1
    if isinstance(p3.returnX(), Pair):
        p4 = p3.returnX()
        p4x = 0
        fromRight += 1
    else:
        p4 = p3.returnY()
        p4x = 1
        fromLeft += 1
    addToLeft = p4.returnX()
    addToRight = p4.returnY()
    if (p4x == 0):
        p3.replaceX(0)
        if addToRight:
            if isinstance(p3.returnY(), Pair):
                done = p3.returnY().addValueToRight(addToRight)
                if done:
                    addToRight = 0
            else:
                p3.replaceY(p3.returnY() + addToRight)
                addToRight = 0
    else:
        p3.replaceY(0)
        if addToLeft:
            if isinstance(p3.returnX(), Pair):
                done = p3.returnX().addValueToLeft(addToLeft)
                if done:
                    addToLeft = 0
            else:
                p3.replaceX(p3.returnX() + addToLeft)
                addToLeft = 0
    if (p3x == 0):
        p2.replaceX(p3)
        if addToRight:
            if isinstance(p2.returnY(), Pair):
                done = p2.returnY().addValueToRight(addToRight)
                if done:
                    addToRight = 0
            else:
                p2.replaceY(p2.returnY() + addToRight)
                addToRight = 0
    else:
        p2.replaceY(p3)
        if addToLeft:
            if isinstance(p2.returnX(), Pair):
                done = p2.returnX().addValueToLeft(addToLeft)
                if done:
                    addToLeft = 0
            else:
                p2.replaceX(p2.returnX() + addToLeft)
                addToLeft = 0

    if (p2x == 0):
        p1.replaceX(p2)
        if addToRight:
            if isinstance(p1.returnY(), Pair):
                done = p1.returnY().addValueToRight(addToRight)
                if done:
                    addToRight = 0
            else:
                p1.replaceY(p1.returnY() + addToRight)
                addToRight = 0
    else:
        p1.replaceY(p2)
        if addToLeft:
            if isinstance(p1.returnX(), Pair):
                done = p1.returnX().addValueToLeft(addToLeft)
                if done:
                    addToLeft = 0
            else:
                p1.replaceX(p1.returnX() + addToLeft)
                addToLeft = 0
    if (p1x == 0):
        p.replaceX(p1)
        if addToRight:
            if isinstance(p.returnY(), Pair):
                done = p.returnY().addValueToRight(addToRight)
                if done:
                    addToRight = 0
            else:
                p.replaceY(p.returnY() + addToRight)
                addToRight = 0
    else:
        p.replaceY(p1)
        if addToLeft:
            if isinstance(p.returnX(), Pair):
                done = p.returnX().addValueToLeft(addToLeft)
                if done:
                    addToLeft = 0
            else:
                p.replaceX(p.returnX() + addToLeft)
                addToLeft = 0
    return p


def split(p):
    px = p.returnX()
    py = p.returnY()
    changed = False
    if (isinstance(px, Pair) and px.containsLarge()) or (isinstance(px, int) and px > 9):
        if isinstance(px, Pair):
            p.replaceX(split(px))
        else:
            new_px = Pair(math.floor(px/2), px-math.floor(px/2))
            p.replaceX(new_px)
    else:
        if isinstance(py, Pair):
            p.replaceY(split(py))
        else:
            new_py = Pair(math.floor(py/2), py-math.floor(py/2))
            p.replaceY(new_py)
    return p


def add_pairs(p1, p2):
    p = Pair(p1, p2)
    while p.returnDepth() > 4 or p.containsLarge():
        if p.returnDepth() > 4:
            p = explode(p)
        else:
            p = split(p)
    return p


def read_pair(s):
    p = s[1:len(s)-1]
    brackets = 0
    if len(p) == 3:
        return Pair(int(p[0]), int(p[2]))
    for i in range(len(p)):
        c = p[i]
        if c == "[":
            brackets += 1
        if c == "]":
            brackets -= 1
        if brackets == 0 and c == ",":
            if len(p[0:i]) == 1:
                p1 = int(p[0])
            else:
                p1 = read_pair(p[0:i])
            if len(p[i+1:len(p)]) == 1:
                p2 = int(p[i+1])
            else:
                p2 = read_pair(p[i+1:len(p)])    
            pair = Pair(p1, p2)
            return pair


def main_a(filename):
    data = lines(filename)
    for i in range(len(data)):
        l = data[i]
        new_pair = read_pair(l.rstrip())
        if i == 0:
            p = new_pair
        else:
            p = add_pairs(p, new_pair)
    return p.magnitude()


def main_b(filename):
    magnitudes = []
    data = lines(filename)
    fishes = []
    for k in range(len(data)):
        l = data[k]
        new_pair = read_pair(l.rstrip())
        fishes.append(new_pair)
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                data = lines(filename)
                fish_i = copy.deepcopy(fishes[i])
                fish_j = copy.deepcopy(fishes[j])
                magnitudes.append(add_pairs(fish_i, fish_j).magnitude())
    magnitudes.sort()
    return max(magnitudes)
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")
