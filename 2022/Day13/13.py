import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 13
test_exp_b = 140


def compare_lists(l1, l2):
  for i in range(len(l1)):
    if i >= len(l2):
      return -1
    if isinstance(l1[i], list) and isinstance(l2[i], list):
      result = compare_lists(l1[i], l2[i])
      if result != 0:
        return result
    elif isinstance(l1[i], list) and not isinstance(l2[i], list):
      temp = [l2[i]]
      result = compare_lists(l1[i], temp)
      if result != 0:
        return result
    elif not isinstance(l1[i], list) and isinstance(l2[i], list):
      temp = [l1[i]]
      result = compare_lists(temp, l2[i])
      if result != 0:
        return result
    else:
      if l1[i] != l2[i]:
        if l1[i] > l2[i]:
          return -1
        else:
          return 1
  if len(l2) > len(l1):
    return 1
  return 0

def swap(l, i, j):
  temp = l[i]
  l[i] = l[j]
  l[j] = temp


def bubbleSort(l):
  for i in range(len(l)-1):
    for j in range(len(l)-i-1):
      if compare_lists(l[j],l[j+1]) == -1:
        swap(l, j, j+1)

def main_a(filename):
  data = load_block(filename)
  result = 0
  for idx, pair in enumerate(data):
    p1, p2 = pair.rstrip().split("\n")
    p1 = json.loads(p1)
    p2 = json.loads(p2)
    r = compare_lists(p1, p2)
    if r == 1:
      result += idx + 1
  return result


def main_b(filename):
  data = lines(filename)
  pairs = [[[2]], [[6]]]
  for l in data:
    l = l.rstrip()
    if l != "":
      pairs.append(json.loads(l))
  bubbleSort(pairs)
  return (pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1)

    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")


