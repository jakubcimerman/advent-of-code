import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 24
test_exp_b = 93


def sgn(x):
  if x >= 0:
    return 1
  if x < 0:
    return -1


def main_a(filename):
  data = lines(filename)
  rocks = []
  min_x = 500
  max_x = 500
  min_y = 0
  max_y = 0
  for path in data:
    points = path.rstrip().split(" -> ")
    l = []
    for p in points:
      x,y = p.split(",")
      x = int(x)
      y = int(y)
      if x < min_x:
        min_x = x
      if x > max_x:
        max_x = x
      if y < min_y:
        min_y = y
      if y > max_y:
        max_y = y
      l.append([x, y])
    rocks.append(l)
  mapa = []
  for y in range(max_y-min_y+4):
    line = []
    for x in range(max_x-min_x+4):
      line.append(".")
    mapa.append(line)
  for rock in rocks:
    for i in range(len(rock)-1):
      for x in range(rock[i][0]-min_x+2,rock[i+1][0]+sgn(rock[i+1][0]-rock[i][0])-min_x+2, sgn(rock[i+1][0]-rock[i][0])):
        for y in range(rock[i][1],rock[i+1][1]+sgn(rock[i+1][1]-rock[i][1]), sgn(rock[i+1][1]-rock[i][1])):
          mapa[y][x] = "#"
  overflow = False
  sand = 0
  while not overflow:
    grain = [500-min_x+2, 0]
    can_move = True
    while can_move:
      if grain[1] >= len(mapa) - 1:
        overflow = True
        can_move = False
        return sand
      elif mapa[grain[1]+1][grain[0]] == ".":
        grain[1] += 1
      elif mapa[grain[1]+1][grain[0]-1] == ".":
        grain[1] += 1
        grain[0] -= 1
      elif mapa[grain[1]+1][grain[0]+1] == ".":
        grain[1] += 1
        grain[0] += 1
      else:
        mapa[grain[1]][grain[0]] = "o"
        sand += 1
        can_move = False



def main_b(filename):
  data = lines(filename)
  rocks = []
  min_x = 500
  max_x = 500
  min_y = 0
  max_y = 0
  for path in data:
    points = path.rstrip().split(" -> ")
    l = []
    for p in points:
      x,y = p.split(",")
      x = int(x)
      y = int(y)
      if x < min_x:
        min_x = x
      if x > max_x:
        max_x = x
      if y < min_y:
        min_y = y
      if y > max_y:
        max_y = y
      l.append([x, y])
    rocks.append(l)
  mapa = []
  for y in range(max_y-min_y+2):
    line = []
    for x in range(3*(max_y-min_y+2)):
      line.append(".")
    mapa.append(line)
  line = []
  for x in range(3*(max_y-min_y+2)):
    line.append("#")
  mapa.append(line)
  middle_x = min_x - int((max_y-min_y+2))
  for rock in rocks:
    for i in range(len(rock)-1):
      for x in range(rock[i][0]-middle_x,rock[i+1][0]+sgn(rock[i+1][0]-rock[i][0])-middle_x, sgn(rock[i+1][0]-rock[i][0])):
        for y in range(rock[i][1],rock[i+1][1]+sgn(rock[i+1][1]-rock[i][1]), sgn(rock[i+1][1]-rock[i][1])):
          mapa[y][x] = "#"
  overflow = False
  sand = 0
  while not overflow:
    grain = [500-middle_x, 0]
    can_move = True
    while can_move:
      if mapa[grain[1]][grain[0]] != ".":
        overflow = True
        can_move = False
        return sand
      elif mapa[grain[1]+1][grain[0]] == ".":
        grain[1] += 1
      elif mapa[grain[1]+1][grain[0]-1] == ".":
        grain[1] += 1
        grain[0] -= 1
      elif mapa[grain[1]+1][grain[0]+1] == ".":
        grain[1] += 1
        grain[0] += 1
      else:
        mapa[grain[1]][grain[0]] = "o"
        sand += 1
        can_move = False

    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")


