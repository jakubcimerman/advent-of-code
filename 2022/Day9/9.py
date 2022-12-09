import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 88
test_exp_b = 36

def sgn(x):
  if x > 0:
    return 1
  if x == 0:
    return 0
  if x < 0:
    return -1

def main_a(filename):
  data = load_strings_split(filename, " ")
  visited_points = []
  H = [0, 0]
  T = [0, 0]
  visited_points.append(T.copy())
  for command in data:
    for i in range(int(command[1])):
      if command[0] == "R":
        H[0] += 1
      if command[0] == "L":
        H[0] -= 1
      if command[0] == "U":
        H[1] += 1
      if command[0] == "D":
        H[1] -= 1
      if abs(H[0] - T[0]) > 1:
        if H[1] == T[1]:
          T[0] += sgn(H[0] - T[0])
        else:
          T[0] += sgn(H[0] - T[0])
          T[1] += sgn(H[1] - T[1])
      if abs(H[1] - T[1]) > 1:
        if H[0] == T[0]:
          T[1] += sgn(H[1] - T[1])
        else:
          T[0] += sgn(H[0] - T[0])
          T[1] += sgn(H[1] - T[1])
      if T not in visited_points:
        visited_points.append(T.copy())
  return len(visited_points)


def main_b(filename):
  data = load_strings_split(filename, " ")
  visited_points = []
  H = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
  visited_points.append([H[9][0], H[9][1]])
  for command in data:
    for i in range(int(command[1])):
      if command[0] == "R":
        H[0][0] += 1
      if command[0] == "L":
        H[0][0] -= 1
      if command[0] == "U":
        H[0][1] += 1
      if command[0] == "D":
        H[0][1] -= 1
      for i in range(1, 10):
        if abs(H[i-1][0] - H[i][0]) > 1:
          if H[i-1][1] == H[i][1]:
            H[i][0] += sgn(H[i-1][0] - H[i][0])
          else:
            H[i][0] += sgn(H[i-1][0] - H[i][0])
            H[i][1] += sgn(H[i-1][1] - H[i][1])
        if abs(H[i-1][1] - H[i][1]) > 1:
          if H[i-1][0] == H[i][0]:
            H[i][1] += sgn(H[i-1][1] - H[i][1])
          else:
            H[i][0] += sgn(H[i-1][0] - H[i][0])
            H[i][1] += sgn(H[i-1][1] - H[i][1])
      if [H[9][0], H[9][1]] not in visited_points:
        visited_points.append([H[9][0], H[9][1]])
  return len(visited_points)
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

