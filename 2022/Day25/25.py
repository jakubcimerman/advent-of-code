import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = "2=-1=0"

def SNAFU_to_dec(SNAFU):
  nums = ["=", "-", "0", "1", "2"]
  result = 0
  for i in range(len(SNAFU)):
    result += pow(5, len(SNAFU) - i - 1) * (nums.index(SNAFU[i]) - 2)
  return result

def dec_to_SNAFU(dec):
  nums = ["=", "-", "0", "1", "2"]
  result = ""
  while dec > 0:
    result += nums[(dec % 5 + 2) % 5]
    dec = int((dec - ((dec % 5 + 2) % 5 - 2)) / 5)
  return result[::-1]


def main_a(filename):
  data = lines(filename)
  result = 0
  for l in data:
    n = SNAFU_to_dec(l.rstrip())
    result += n
  return dec_to_SNAFU(result)


test_and_submit(main_a, DAY, test_exp_a, "a")
