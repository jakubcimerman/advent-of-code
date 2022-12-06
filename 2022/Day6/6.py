import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 7
test_exp_b = 19

def check_if_repeated(used):
  repeated = False
  for i in range(len(used)-1):
    for j in range(i+1,len(used)):
      if used[i] == used[j]:
        repeated = True
  return repeated

def main_a(filename):
  data = file(filename).rstrip()
  used = [data[0]]
  for i in range(1,4):
    used.append(data[i])
  if not check_if_repeated(used):
    return 4
  for i in range(4,len(data)):
    used.pop(0)
    used.append(data[i])
    if not check_if_repeated(used):
      return i+1


def main_b(filename):
  data = file(filename).rstrip()
  used = [data[0]]
  for i in range(1,14):
    used.append(data[i])
  if not check_if_repeated(used):
    return 4
  for i in range(14,len(data)):
    used.pop(0)
    used.append(data[i])
    if not check_if_repeated(used):
      return i+1
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

