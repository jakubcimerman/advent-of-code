import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 24000
test_exp_b = 45000


def main_a(filename):
    data = load_block(filename)
    max_cal = 0
    for elf in data:
      elf = elf.split('\n')
      carrying = 0
      for food in elf:
        carrying += int(food.rstrip())
      if carrying > max_cal:
        max_cal = carrying
    return max_cal


def main_b(filename):
    data = load_block(filename)
    calories = []
    for elf in data:
      elf = elf.split('\n')
      carrying = 0
      for food in elf:
        carrying += int(food.rstrip())
      calories.append(carrying)
    calories.sort(reverse = True)
    return calories[0] + calories[1] + calories[2]
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

