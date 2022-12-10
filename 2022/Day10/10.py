import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 13140
test_exp_b = 0


def main_a(filename):
  data = lines(filename)
  total = 0
  cycle = 0
  X = 1
  for l in data:
    if l[0] == "n":
      cycle += 1
      if cycle % 40 == 20:
        total += X*cycle
    if l[0] == "a":
      cycle += 1
      if cycle % 40 == 20:
        total += X*cycle
      cycle += 1
      if cycle % 40 == 20:
        total += X*cycle
      a, b = l.rstrip().split(" ")
      X += int(b)
  return total



def main_b(filename):
  data = lines(filename)
  cycle = 0
  X = 1
  result = ""
  for l in data:
    if l[0] == "n":
      if abs(cycle%40-X) < 2:
        result += "#"
      else:
        result += "."
      if cycle % 40 == 39:
        result += "\n"
      cycle += 1         
    if l[0] == "a":
      if abs(cycle%40-X) < 2:
        result += "#"
      else:
        result += "."
      if cycle % 40 == 39:
        result += "\n"
      cycle += 1
      if abs(cycle%40-X) < 2:
        result += "#"
      else:
        result += "."
      if cycle % 40 == 39:
        result += "\n"
      cycle += 1
      a, b = l.rstrip().split(" ")
      X += int(b)
  print(result)
  return 
    

test_and_submit(main_a, DAY, test_exp_a, "a")
main_b(f"{DAY}.txt")

