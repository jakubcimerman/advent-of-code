import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math

DAY = datetime.date.today().day
test_exp_a = 31
test_exp_b = 29

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "E"]


def main_a(filename):
  data = load_map_ll(filename)
  data = add_array_border(data, "z")
  to_visit = []
  visited = []
  for i in range(len(data)):
    for j in range(len(data[i])):
      if data[i][j] == "S":
        to_visit.append([i, j, 0])
        data[i][j] = "a"
      if data[i][j] == "E":
        data[i][j] = "z"
        fin_i = i
        fin_j = j
  while len(to_visit) > 0:
    i, j, d = to_visit[0]
    to_visit.pop(0)
    if i == fin_i and j == fin_j:
      return d
    for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
      if [ni, nj] not in visited and alphabet.index(data[ni][nj]) < alphabet.index(data[i][j]) + 2:
        visited.append([ni, nj])
        to_visit.append([ni, nj, d+1])

def partb(data, i, j, fin_i, fin_j):
  to_visit = []
  visited = []
  to_visit.append([i, j, 0])
  while len(to_visit) > 0:
    i, j, d = to_visit[0]
    to_visit.pop(0)
    if i == fin_i and j == fin_j:
      return d
    for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
      if [ni, nj] not in visited and alphabet.index(data[ni][nj]) < alphabet.index(data[i][j]) + 2:
        visited.append([ni, nj])
        to_visit.append([ni, nj, d+1])

def main_b(filename):
  data = load_map_ll(filename)
  data = add_array_border(data, "z")
  for i in range(len(data)):
    for j in range(len(data[i])):
      if data[i][j] == "S":
        data[i][j] = "a"
      if data[i][j] == "E":
        data[i][j] = "z"
        fin_i = i
        fin_j = j
  distances = []
  for a in range(1,len(data)-1):
    distances.append(partb(data, a, 1, fin_i, fin_j))
  return(min(distances))

    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")


