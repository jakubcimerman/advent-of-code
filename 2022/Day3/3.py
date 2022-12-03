import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 157
test_exp_b = 70

def value(c):
  a = ord(c)
  if a > 64 and a < 91:
    a -= 38
  if a > 96 and a < 123:
    a -= 96
  return a

def main_a(filename):
  data = lines(filename)
  skore = 0
  for line in data:
    rucksack1 = line[0:int(len(line)/2)]
    rucksack2 = line[int(len(line)/2):len(line)]
    used = []
    for c in rucksack1:
      if c in rucksack2 and c not in used:
        used.append(c)
        skore += value(c)
  return skore


def main_b(filename):
  data = lines(filename)
  skore = 0
  for i in range(int(len(data)/3)):
    rucksack1 = data[i*3].rstrip()
    rucksack2 = data[i*3+1].rstrip()
    rucksack3 = data[i*3+2].rstrip()
    used = []
    for c in rucksack1:
      if c in rucksack2 and c in rucksack3 and c not in used:
        used.append(c)
        skore += value(c)
  return skore
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

