import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 95437
test_exp_b = 24933642

dirsizes = []

def find_size_of_directory(data, d, path):
  dirsize = 0
  current_path = []
  N = len(data)
  for i in range(N):
    if data[i][1] == "cd":
      if data[i][2] == "..":
        current_path.pop() 
      else:
        current_path.append(data[i][2])
    if len(data[i]) == 3 and data[i][2] == d and current_path[:-1] == path:
      for j in range(i+2, N):
        if data[j][0].isnumeric():
          dirsize += int(data[j][0])
        if data[j][0] == "dir":
          dirsize += find_size_of_directory(data, data[j][1], current_path)
        if data[j][0] == "$":
          break
  dirsizes.append([path.copy(), d, dirsize])
  return dirsize


def main_a(filename):
  data = load_strings_split(filename, " ")
  dirsizes.clear()
  current_path = []
  find_size_of_directory(data, '/', current_path)
  total = 0
  for n in dirsizes:
    if n[2] <= 100000:
      total += n[2]
  return total


def main_b(filename):
  data = load_strings_split(filename, " ")
  dirsizes.clear()
  current_path = []
  find_size_of_directory(data, '/', current_path)
  needs_to_clear = dirsizes[len(dirsizes)-1][2] - (70000000 - 30000000)
  best_dir = 70000000
  for n in dirsizes:
    if n[2] >= needs_to_clear and n[2] < best_dir:
      best_dir = n[2]
  return best_dir
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

