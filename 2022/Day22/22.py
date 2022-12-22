import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 6032
test_exp_b = 5031

directions = [[1,0], [0,1], [-1,0], [0,-1]]


def main_a(filename):
  data = lines(filename)
  mapa = {}
  max_x = 0
  max_y = len(data) - 2
  for y in range(len(data)-1):
    if len(data[y]) > max_x:
      max_x = len(data[y])
    for x in range(len(data[y])):
      if data[y][x] == "." or data[y][x] == "#":
        mapa[(x+1,y+1)] = data[y][x]
  pos = [list(mapa.keys())[0][0], list(mapa.keys())[0][1]]
  face = directions[0]
  commands = data[-1].rstrip()
  move = 0
  i = 0
  while i < len(commands):
    if commands[i].isdigit():
      j = 1
      while True:
        if i + j >= len(commands) or not commands[i+j].isdigit():
          break
        j += 1
      move = int(commands[i:i+j])
      for m in range(move):
        pos[0] += face[0]
        pos[1] += face[1]
        if (pos[0], pos[1]) not in mapa:
          if face == [1, 0]:
            for x in range(1,max_x):
              if (x, pos[1]) in mapa:
                if mapa[(x, pos[1])] == "#":
                  pos[0] -= face[0]
                else:
                  pos[0] = x
                break
          if face == [-1, 0]:
            for x in range(max_x,0,-1):
              if (x, pos[1]) in mapa:
                if mapa[(x, pos[1])] == "#":
                  pos[0] -= face[0]
                else:
                  pos[0] = x
                break
          if face == [0, 1]:
            for y in range(1,max_y):
              if (pos[0], y) in mapa:
                if mapa[(pos[0], y)] == "#":
                  pos[1] -= face[1]
                else:
                  pos[1] = y
                break
          if face == [0, -1]:
            for y in range(max_y, 0, -1):
              if (pos[0], y) in mapa:
                if mapa[(pos[0], y)] == "#":
                  pos[1] -= face[1]
                else:
                  pos[1] = y
                break
        elif mapa[(pos[0], pos[1])] == "#":
          pos[0] -= face[0]
          pos[1] -= face[1]
          break
      i += j - 1
    elif commands[i] == "R":
      face = directions[(directions.index(face) + 1) % len(directions)]
    elif commands[i] == "L":
      face = directions[(directions.index(face) - 1) % len(directions)]
    i += 1
  return 1000 * pos[1] + 4 * pos[0] + directions.index(face)


# Part b has specific transition between faces of cube, so I did it specifically to solve my input, not any general input
def main_b(filename):
  data = lines(filename)
  mapa = {}
  max_x = 0
  max_y = len(data) - 2
  for y in range(len(data)-1):
    if len(data[y]) > max_x:
      max_x = len(data[y])
    for x in range(len(data[y])):
      if data[y][x] == "." or data[y][x] == "#":
        mapa[(x+1,y+1)] = data[y][x]
  square = int(math.sqrt(max_x * max_y / 12))
  pos = [list(mapa.keys())[0][0], list(mapa.keys())[0][1]]
  face = directions[0]
  commands = data[-1].rstrip()
  move = 0
  i = 0
  while i < len(commands):
    if commands[i].isdigit():
      j = 1
      while True:
        if i + j >= len(commands) or not commands[i+j].isdigit():
          break
        j += 1
      move = int(commands[i:i+j])
      for m in range(move):
        pos[0] += face[0]
        pos[1] += face[1]
        if (pos[0], pos[1]) not in mapa:
          if face == directions[0]:
            if pos[1] <= 50:
              new_pos = [100, 151-pos[1]]
              face = directions[2]
            elif pos[1] <= 100:
              new_pos = [pos[1]+50, 50]
              face = directions[3]
            elif pos[1] <= 150:
              new_pos = [150, 151-pos[1]]
              face = directions[2]
            else:
              new_pos = [pos[1]-100, 150]
              face = directions[3]
            if mapa[(new_pos[0], new_pos[1])] == "#":
              face = directions[0]
              pos[0] -= face[0]
              break
            else:
              pos = new_pos
          elif face == directions[1]:
            if pos[0] <= 50:
              new_pos = [100+pos[0], 1]
              face = directions[1]
            elif pos[0] <= 100:
              new_pos = [50, 100+pos[0]]
              face = directions[2]
            else:
              new_pos = [100, pos[0]-50]
              face = directions[2]
            if mapa[(new_pos[0], new_pos[1])] == "#":
              face = directions[1]
              pos[1] -= face[1]
              break
            else:
              pos = new_pos
          elif face == directions[2]:
            if pos[1] <= 50:
              new_pos = [1, 151-pos[1]]
              face = directions[0]
            elif pos[1] <= 100:
              new_pos = [pos[1]-50, 101]
              face = directions[1]
            elif pos[1] <= 150:
              new_pos = [51, 151-pos[1]]
              face = directions[0]
            else:
              new_pos = [pos[1]-100, 1]
              face = directions[1]
            if mapa[(new_pos[0], new_pos[1])] == "#":
              face = directions[2]
              pos[0] -= face[0]
              break
            else:
              pos = new_pos
          elif face == directions[3]:
            if pos[0] <= 50:
              new_pos = [51, pos[0]+50]
              face = directions[0]
            elif pos[0] <= 100:
              new_pos = [1, 100+pos[0]]
              face = directions[0]
            else:
              new_pos = [pos[0]-100, 200]
              face = directions[3]
            if mapa[(new_pos[0], new_pos[1])] == "#":
              face = directions[3]
              pos[1] -= face[1]
              break
            else:
              pos = new_pos
        elif mapa[(pos[0], pos[1])] == "#":
          pos[0] -= face[0]
          pos[1] -= face[1]
          break
      i += j - 1
    elif commands[i] == "R":
      face = directions[(directions.index(face) + 1) % len(directions)]
    elif commands[i] == "L":
      face = directions[(directions.index(face) - 1) % len(directions)]
    i += 1
  return 1000 * pos[1] + 4 * pos[0] + directions.index(face)


test_and_submit(main_a, DAY, test_exp_a, "a")
print(main_b("22.txt"))