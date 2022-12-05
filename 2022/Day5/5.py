import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = "CMZ"
test_exp_b = "MCD"

def main_a(filename):
  data = load_block(filename)
  crates = data[0].split("\n")
  N = len(crates[len(crates)-1].split("  "))
  stacks = []
  for i in range(N):
    stacks.append([])
  for i in range(len(crates)-1):
    for j in range(N):
      if crates[len(crates)-2-i][4*j+1] != " ":
        stacks[j].append(crates[len(crates)-2-i][4*j+1])
  commands = data[1].split("\n")
  for c in commands:
    c = c.split(" ")
    num = int(c[1])
    fr = int(c[3])
    to = int(c[5])
    for i in range(num):
      stacks[to-1].append(stacks[fr-1][len(stacks[fr-1])-1])
      stacks[fr-1].pop()
  result = ""
  for i in range(N):
    result += stacks[i][-1]
  return result


def main_b(filename):
  data = load_block(filename)
  crates = data[0].split("\n")
  N = len(crates[len(crates)-1].split("  "))
  stacks = []
  for i in range(N):
    stacks.append([])
  for i in range(len(crates)-1):
    for j in range(N):
      if crates[len(crates)-2-i][4*j+1] != " ":
        stacks[j].append(crates[len(crates)-2-i][4*j+1])
  commands = data[1].split("\n")
  for c in commands:
    c = c.split(" ")
    num = int(c[1])
    fr = int(c[3])
    to = int(c[5])
    for i in range(num):
      stacks[to-1].append(stacks[fr-1][len(stacks[fr-1])-1-num+1+i])
    for i in range(num):
      stacks[fr-1].pop()
  result = ""
  for i in range(N):
    result += stacks[i][-1]
  return result
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

