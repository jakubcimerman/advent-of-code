import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 110
test_exp_b = 20

def print_elfs(data):
  mapa = ""
  n = 0
  for y in range(len(data)):
    for x in range(len(data[y])):
      if data[y][x] == "#":
        n += 1
      mapa += data[y][x]
    mapa += "\n"
  print(mapa)

def main_a(filename):
  dirs = [[[-1,-1], [0,-1], [1,-1]], [[-1, 1], [0, 1], [1, 1]], [[-1, -1], [-1, 0], [-1, 1]], [[1, -1], [1, 0], [1, 1]]]
  around = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
  data = load_map_ll(filename)
  N = 0
  elfs = {}
  for y in range(len(data)):
    for x in range(len(data[y])):
      if data[y][x] == "#":
        elfs[N] = {
          "x": x,
          "y": y,
          "move_to": []
        }
        N += 1
  for r in range(10):
    data = add_array_border(data, ".")
    for i in range(N):
      elfs[i]["x"] += 1
      elfs[i]["y"] += 1
    for i in range(N):
      will_move = False
      for a in around:
        if data[elfs[i]["y"]+a[1]][elfs[i]["x"]+a[0]] == "#":
          will_move = True
          break
      if not will_move:
        continue
      for d in dirs:
        can_move_here = True
        for p in d:
          if data[elfs[i]["y"]+p[1]][elfs[i]["x"]+p[0]] == "#":
            can_move_here = False
        if can_move_here:
          elfs[i]["move_to"] = [elfs[i]["x"]+d[1][0], elfs[i]["y"]+d[1][1]]
          break
    moved_elfs = 0
    for i in range(N):
      can_move_here = True
      if elfs[i]["move_to"] == []:
        continue
      for j in range(N):
        if elfs[i]["move_to"] == elfs[j]["move_to"] and i != j:
          can_move_here = False
          break
      if not can_move_here:
        continue
      else:
        moved_elfs += 1
        data[elfs[i]["y"]][elfs[i]["x"]] = "."
        data[elfs[i]["move_to"][1]][elfs[i]["move_to"][0]] = "#"
        elfs[i]["x"] = elfs[i]["move_to"][0]
        elfs[i]["y"] = elfs[i]["move_to"][1]
    for i in range(N):
      elfs[i]["move_to"] = []
    d = dirs[0]
    dirs.pop(0)
    dirs.append(d)
  min_x = 100000
  max_x = 0
  min_y = 100000
  max_y = 0
  for i in range(N):
    if elfs[i]["x"] > max_x:
      max_x = elfs[i]["x"]
    if elfs[i]["x"] < min_x:
      min_x = elfs[i]["x"]
    if elfs[i]["y"] > max_y:
      max_y = elfs[i]["y"]
    if elfs[i]["y"] < min_y:
      min_y = elfs[i]["y"]
  return (max_x-min_x+1)*(max_y-min_y+1)-N


def main_b(filename):
  dirs = [[[-1,-1], [0,-1], [1,-1]], [[-1, 1], [0, 1], [1, 1]], [[-1, -1], [-1, 0], [-1, 1]], [[1, -1], [1, 0], [1, 1]]]
  around = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
  data = load_map_ll(filename)
  N = 0
  elfs = {}
  for y in range(len(data)):
    for x in range(len(data[y])):
      if data[y][x] == "#":
        elfs[N] = {
          "x": x,
          "y": y,
          "move_to": []
        }
        N += 1
  data = add_array_border(data, ".")
  for i in range(N):
    elfs[i]["x"] += 1
    elfs[i]["y"] += 1
  for r in range(100000):
    for i in range(N):
      will_move = False
      for a in around:
        if data[elfs[i]["y"]+a[1]][elfs[i]["x"]+a[0]] == "#":
          will_move = True
          break
      if not will_move:
        continue
      for d in dirs:
        can_move_here = True
        for p in d:
          if data[elfs[i]["y"]+p[1]][elfs[i]["x"]+p[0]] == "#":
            can_move_here = False
        if can_move_here:
          elfs[i]["move_to"] = [elfs[i]["x"]+d[1][0], elfs[i]["y"]+d[1][1]]
          break
    moved_elfs = 0
    for i in range(N):
      can_move_here = True
      if elfs[i]["move_to"] == []:
        continue
      for j in range(N):
        if elfs[i]["move_to"] == elfs[j]["move_to"] and i != j:
          can_move_here = False
          break
      if not can_move_here:
        continue
      else:
        moved_elfs += 1
        data[elfs[i]["y"]][elfs[i]["x"]] = "."
        data[elfs[i]["move_to"][1]][elfs[i]["move_to"][0]] = "#"
        elfs[i]["x"] = elfs[i]["move_to"][0]
        elfs[i]["y"] = elfs[i]["move_to"][1]
    if moved_elfs == 0:
      return r+1
    for i in range(N):
      elfs[i]["move_to"] = []
    d = dirs[0]
    dirs.pop(0)
    dirs.append(d)
    min_x = 100000
    max_x = 0
    min_y = 100000
    max_y = 0
    for i in range(N):
      if elfs[i]["x"] > max_x:
        max_x = elfs[i]["x"]
      if elfs[i]["x"] < min_x:
        min_x = elfs[i]["x"]
      if elfs[i]["y"] > max_y:
        max_y = elfs[i]["y"]
      if elfs[i]["y"] < min_y:
        min_y = elfs[i]["y"]
    if min_y < 2 or min_x < 2 or max_y > len(data)-3 or max_x > len(data[0])-3:
      data = add_array_border(data, ".")
      for i in range(N):
        elfs[i]["x"] += 1
        elfs[i]["y"] += 1
  return (max_x-min_x+1)*(max_y-min_y+1)-N



test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")
