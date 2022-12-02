import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 15
test_exp_b = 12

def main_a(filename):
  player = {
    "X": 1,
    "Y": 2,
    "Z": 3
  }

  outcome = {
    "X": {
      "A": 3,
      "B": 0,
      "C": 6
    },
    "Y": {
      "A": 6,
      "B": 3,
      "C": 0
    },
    "Z": {
      "A": 0,
      "B": 6,
      "C": 3
    }
  }
  data = lines(filename)
  skore = 0
  for game in data:
    a, b = game.rstrip().split(" ")
    skore += player[b] + outcome[b][a]
  return skore


def main_b(filename):
  outcome = {
    "X": 0,
    "Y": 3,
    "Z": 6
  }

  player = {
    "X": {
      "A": 3,
      "B": 1,
      "C": 2
    },
    "Y": {
      "A": 1,
      "B": 2,
      "C": 3
    },
    "Z": {
      "A": 2,
      "B": 3,
      "C": 1
    }
  }
  data = lines(filename)
  skore = 0
  for game in data:
    a, b = game.rstrip().split(" ")
    skore += outcome[b] + player[b][a]
  return skore
    

#test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

