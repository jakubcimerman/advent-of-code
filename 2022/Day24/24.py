import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 18
test_exp_b = 54


def move_blizzards(blizzards, max_x, max_y):
  for i in range(len(blizzards)):
    blizzards[i]["x"] += blizzards[i]["dir"][0]
    blizzards[i]["y"] += blizzards[i]["dir"][1]
    if blizzards[i]["x"] == 0:
      blizzards[i]["x"] = max_x - 2
    if blizzards[i]["x"] == max_x - 1:
      blizzards[i]["x"] = 1
    if blizzards[i]["y"] == 0:
      blizzards[i]["y"] = max_y - 2
    if blizzards[i]["y"] == max_y - 1:
      blizzards[i]["y"] = 1
  return

def is_blizzard(blizzards, x, y):
  for i in range(len(blizzards)):
    if blizzards[i]["x"] == x and blizzards[i]["y"] == y:
      return True
  return False

def print_map(blizzards, max_x, max_y, player):
  result = ""
  for y in range(max_y):
    for x in range(max_x):
      if [x, y] == player and is_blizzard(blizzards, x, y):
        result += "R"
      elif [x, y] == player:
        result += "E"
      elif is_blizzard(blizzards, x, y):
        result += "B"
      elif x == 0 or x == max_x-1 or y == 0 or y == max_y-1:
        result += "#"
      else:
        result += "."  
    result += "\n"
  print(result)

def main_a(filename):
  dirs = [[0, 0], [0,-1], [0, 1], [-1, 0], [1, 0]]
  data = load_map_ll(filename)
  N = 0
  blizzards = {}
  for y in range(len(data)):
    for x in range(len(data[y])):
      if data[y][x] == ">":
        blizzards[N] = {
          "x": x,
          "y": y,
          "dir": [1, 0]
        }
        N += 1
      if data[y][x] == "<":
        blizzards[N] = {
          "x": x,
          "y": y,
          "dir": [-1, 0]
        }
        N += 1
      if data[y][x] == "^":
        blizzards[N] = {
          "x": x,
          "y": y,
          "dir": [0, -1]
        }
        N += 1
      if data[y][x] == "v":
        blizzards[N] = {
          "x": x,
          "y": y,
          "dir": [0, 1]
        }
        N += 1
  current_time = -1
  visited = []
  to_visit = []
  to_visit.append([1, 0, 0])
  while len(to_visit) > 0:
    #print(to_visit)
    x, y, t = to_visit[0]
    to_visit.pop(0)
    visited.append([x, y, t])
    #print(to_visit)
    if t > current_time:
      print(t, len(to_visit))
      move_blizzards(blizzards, len(data[0]), len(data))
      current_time = t
    #print(x, y, t)
    #print(visited)
    #print_map(blizzards, len(data[0]), len(data), [x, y])
    #if is_blizzard(blizzards, x, y):
      #continue
    for d in dirs:
      new_state = [x+d[0], y+d[1], t+1]
      if x+d[0] == len(data[0])-2 and y+d[1] == len(data)-1:
        return t + 1
      if not is_blizzard(blizzards, x + d[0], y + d[1]):
        if x+d[0] > 0 and y+d[1] > 0 and x+d[0] < len(data[0])-1 and y+d[1] < len(data)-1:
          if new_state not in visited and new_state not in to_visit:
            to_visit.append(new_state)
        elif x+d[0] == 1 and y+d[1] == 0 and t < 20:
          if new_state not in visited and new_state not in to_visit:
            to_visit.append(new_state)


def main_b(filename):
  dirs = [[0, 0], [0,-1], [0, 1], [-1, 0], [1, 0]]
  data = load_map_ll(filename)
  N = 0
  blizzards = {}
  for y in range(len(data)):
    for x in range(len(data[y])):
      if data[y][x] == ">":
        blizzards[N] = {
          "x": x,
          "y": y,
          "dir": [1, 0]
        }
        N += 1
      if data[y][x] == "<":
        blizzards[N] = {
          "x": x,
          "y": y,
          "dir": [-1, 0]
        }
        N += 1
      if data[y][x] == "^":
        blizzards[N] = {
          "x": x,
          "y": y,
          "dir": [0, -1]
        }
        N += 1
      if data[y][x] == "v":
        blizzards[N] = {
          "x": x,
          "y": y,
          "dir": [0, 1]
        }
        N += 1
  current_time = -1
  visited = []
  to_visit = []
  to_visit.append([1, 0, 0])
  trip_part = 1
  while len(to_visit) > 0:
    #print(to_visit)
    x, y, t = to_visit[0]
    to_visit.pop(0)
    visited.append([x, y, t])
    #print(to_visit)
    if t > current_time:
      print(t, len(to_visit))
      move_blizzards(blizzards, len(data[0]), len(data))
      current_time = t
    #print(x, y, t)
    #print(visited)
    #print_map(blizzards, len(data[0]), len(data), [x, y])
    #if is_blizzard(blizzards, x, y):
      #continue
    for d in dirs:
      new_state = [x+d[0], y+d[1], t+1]
      if trip_part == 1 and x+d[0] == len(data[0])-2 and y+d[1] == len(data)-1:
        visited.clear()
        to_visit.clear()
        to_visit.append([len(data[0])-2, len(data)-1, t+1])
        trip_part = 2
        print("end")
        break
      elif trip_part == 2 and x+d[0] == 1 and y+d[1] == 0:
        visited.clear()
        to_visit.clear()
        to_visit.append([1, 0, t+1])
        trip_part = 3
        print("start")
        break
      elif trip_part == 3:
        if x+d[0] == len(data[0])-2 and y+d[1] == len(data)-1:
          return t + 1
      if not is_blizzard(blizzards, x + d[0], y + d[1]):
        if x+d[0] > 0 and y+d[1] > 0 and x+d[0] < len(data[0])-1 and y+d[1] < len(data)-1:
          if new_state not in visited and new_state not in to_visit:
            to_visit.append(new_state)
        elif (x+d[0] == 1 and y+d[1] == 0) or (x+d[0] == len(data[0])-2 and y+d[1] == len(data)-1):
          if new_state not in visited and new_state not in to_visit:
            to_visit.append(new_state)



#test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")
