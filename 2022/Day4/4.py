import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 2
test_exp_b = 4

def main_a(filename):
  data = lines(filename)
  overlapped_pairs = 0
  for line in data:
    a, b = line.rstrip().split(",")
    elf1 = a.split("-")
    elf2 = b.split("-")
    if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
      overlapped_pairs += 1
    elif int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
      overlapped_pairs += 1
  return overlapped_pairs


def main_b(filename):
  data = lines(filename)
  overlapped_pairs = 0
  for line in data:
    a, b = line.rstrip().split(",")
    elf1 = a.split("-")
    elf2 = b.split("-")
    if int(elf1[1]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]):
      overlapped_pairs += 1
    elif int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[0]):
      overlapped_pairs += 1
  return overlapped_pairs
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

