import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 21
test_exp_b = 8


def main_a(filename):
  data = load_map_ll(filename)
  seen_trees = []
  for i in range(len(data)):
    for j in range(len(data)):
      seen = True
      for k in range(j):
        if int(data[i][k]) >= int(data[i][j]):
          seen = False
      if seen:
        if [i, j] not in seen_trees:
          seen_trees.append([i, j])
    for j in range(len(data)-1, -1, -1):
      seen = True
      for k in range(len(data)-1, j, -1):
        if int(data[i][k]) >= int(data[i][j]):
          seen = False
      if seen:
        if [i, j] not in seen_trees:
          seen_trees.append([i, j])
    for j in range(len(data)):
      seen = True
      for k in range(j):
        if int(data[k][i]) >= int(data[j][i]):
          seen = False
      if seen:
        if [j, i] not in seen_trees:
          seen_trees.append([j, i])
    for j in range(len(data)-1, -1, -1):
      seen = True
      for k in range(len(data)-1, j, -1):
        if int(data[k][i]) >= int(data[j][i]):
          seen = False
      if seen:
        if [j, i] not in seen_trees:
          seen_trees.append([j, i])
  return len(seen_trees)



def main_b(filename):
  data = load_map_ll(filename)
  best_score = 0
  for i in range(len(data)):
    for j in range(len(data)):
      current_score = 1
      side1 = 0
      side2 = 0
      side3 = 0
      side4 = 0
      for k in range(j-1, -1, -1):
        print(j, k)
        if int(data[i][k]) < int(data[i][j]):
          side1 += 1
        else:
          side1 += 1
          break
      for k in range(j+1, len(data)):
        if int(data[i][k]) < int(data[i][j]):
          side2 += 1
        else:
          side2 += 1
          break
      for k in range(i-1, -1, -1):
        if int(data[k][j]) < int(data[i][j]):
          side3 += 1
        else:
          side3 += 1
          break
      for k in range(i+1, len(data)):
        if int(data[k][j]) < int(data[i][j]):
          side4 += 1
        else:
          side4 += 1
          break
      current_score = side1*side2*side3*side4
      if current_score > best_score:
        best_score = current_score
  return best_score
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

