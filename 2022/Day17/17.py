import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 3068
test_exp_b = 1514285714288

shapes = [
  {
    "w": 4,
    "h": 1,
    "r": [["#", "#", "#", "#"]]
  },
  {
    "w": 3,
    "h": 3,
    "r": [[".", "#", "."], ["#", "#", "#"], [".", "#", "."]]
  },
  {
    "w": 3,
    "h": 3,
    "r": [["#", "#", "#"], [".", ".", "#"], [".", ".", "#"]]
  },
  {
    "w": 1,
    "h": 4,
    "r": [["#"], ["#"], ["#"], ["#"]]
  },
  {
    "w": 2,
    "h": 2,
    "r": [["#", "#"], ["#", "#"]]
  },
]

def find_highest_rock(cave):
  for i in range(1,len(cave)):
    empty_line = True
    for j in range(1, len(cave[1]) - 1):
      if cave[i][j] != ".":
        empty_line = False
        break
    if empty_line:
      return i
  return 0

def move_rock(cave, x, y, s, d):
  moved = False
  can_move = True
  if d == ">":
    for i in range(s["w"]):
      for j in range(s["h"]):
        if s["r"][j][i] == "#" and cave[y+j][x+i+1] != ".":
          can_move = False
    if can_move:
      x += 1
      moved = True
  if d == "<":
    for i in range(s["w"]):
      for j in range(s["h"]):
        if s["r"][j][i] == "#" and cave[y+j][x+i-1] != ".":
          can_move = False
    if can_move:
      x -= 1
      moved = True
  if d == "v":
    for i in range(s["w"]):
      for j in range(s["h"]):
        if s["r"][j][i] == "#" and cave[y+j-1][x+i] != ".":
          can_move = False
    if can_move:
      y -= 1
      moved = True
  return [x, y, moved]

def print_cave(cave):
  c = ""
  for i in range(len(cave)-1, -1, -1):
    l = ""
    for j in range(len(cave[1])):
      l += cave[i][j]
    c += l + "\n"
  print(c)
  return

def shape(cave):
  h = find_highest_rock(cave)
  result = []
  for j in range(1, len(cave[1]) - 1):
    for i in range(h, 0, -1):
      if cave[i][j] != ".":
        result.append(h-i)
        break
  return result

def main_a(filename):
  moves = file(filename).rstrip()
  moves_counter = 0
  cave_width = 7
  cave = []
  for i in range(5):
    line = []
    for j in range(cave_width + 2):
      if i == 0:
        line.append("-")
      elif j == 0 or j == cave_width + 1:
        line.append("|")
      else:
        line.append(".")
    cave.append(line)
  for t in range(2022):
    s = shapes[t % len(shapes)]
    h = find_highest_rock(cave)
    if len(cave) < h + s["h"] + 3:
      for i in range(h + s["h"] + 3 - len(cave)):
        line = []
        for j in range(cave_width + 2):
          if j == 0 or j == cave_width + 1:
            line.append("|")
          else:
            line.append(".")
        cave.append(line)
    x = 3
    y = h + 3
    can_fall = True
    while can_fall:
      move = moves[moves_counter]
      moves_counter = (moves_counter + 1) % len(moves)
      x, y, moved = move_rock(cave, x, y, s, move)
      x, y, can_fall = move_rock(cave, x, y, s, "v")
    for i in range(s["w"]):
      for j in range(s["h"]):
        if s["r"][j][i] == "#":
          cave[y+j][x+i] = s["r"][j][i]
  return find_highest_rock(cave)-1



def main_b(filename):
  moves = file(filename).rstrip()
  moves_counter = 0
  cave_width = 7
  cave = []
  for i in range(5):
    line = []
    for j in range(cave_width + 2):
      if i == 0:
        line.append("-")
      elif j == 0 or j == cave_width + 1:
        line.append("|")
      else:
        line.append(".")
    cave.append(line)
  starting_states = []
  additional_info = []
  repetition = {"state": []}
  # first loop to find the repetition pattern
  for t in range(10000):
    s = shapes[t % len(shapes)]
    h = find_highest_rock(cave)
    sh = shape(cave)
    state = [t % len(shapes), moves_counter, sh]
    if state not in starting_states:
      starting_states.append(state)
      additional_info.append([t, h])
    elif repetition["state"] == []:
      repetition = {
        "state": state,
        "start": additional_info[starting_states.index(state)][0]+1,
        "period": t - additional_info[starting_states.index(state)][0],
        "height": h - additional_info[starting_states.index(state)][1],
        "t": t,
        "h": h 
      }
      break
    if len(cave) < h + s["h"] + 3:
      for i in range(h + s["h"] + 3 - len(cave)):
        line = []
        for j in range(cave_width + 2):
          if j == 0 or j == cave_width + 1:
            line.append("|")
          else:
            line.append(".")
        cave.append(line)
    x = 3
    y = h + 3
    can_fall = True
    while can_fall:
      move = moves[moves_counter]
      moves_counter = (moves_counter + 1) % len(moves)
      x, y, moved = move_rock(cave, x, y, s, move)
      x, y, can_fall = move_rock(cave, x, y, s, "v")
    for i in range(s["w"]):
      for j in range(s["h"]):
        if s["r"][j][i] == "#":
          cave[y+j][x+i] = s["r"][j][i]
  print(repetition)
  cave.clear()
  for i in range(5):
    line = []
    for j in range(cave_width + 2):
      if i == 0:
        line.append("-")
      elif j == 0 or j == cave_width + 1:
        line.append("|")
      else:
        line.append(".")
    cave.append(line)
  moves_counter = 0
  t_max = 1000000000000
  # now the second loop - but only up to the start of the repetition pattern, then add hieght 
  # of N repetitions, and then continue with the rest of the time steps
  N = math.floor((t_max - repetition["start"]) / repetition["period"])
  add_height = repetition["height"] * N
  T = repetition["start"] + (t_max - repetition["start"]) % repetition["period"]
  for t in range(T):
    s = shapes[t % len(shapes)]
    h = find_highest_rock(cave)
    if len(cave) < h + s["h"] + 3:
      for i in range(h + s["h"] + 3 - len(cave)):
        line = []
        for j in range(cave_width + 2):
          if j == 0 or j == cave_width + 1:
            line.append("|")
          else:
            line.append(".")
        cave.append(line)
    x = 3
    y = h + 3
    can_fall = True
    while can_fall:
      move = moves[moves_counter]
      moves_counter = (moves_counter + 1) % len(moves)
      x, y, moved = move_rock(cave, x, y, s, move)
      x, y, can_fall = move_rock(cave, x, y, s, "v")
    for i in range(s["w"]):
      for j in range(s["h"]):
        if s["r"][j][i] == "#":
          cave[y+j][x+i] = s["r"][j][i]
  return find_highest_rock(cave) - 1 + add_height

    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

