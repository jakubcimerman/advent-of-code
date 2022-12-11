import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math

DAY = datetime.date.today().day
test_exp_a = 10605
test_exp_b = 2713310158

monkeys = []
total_test = 1

class Monkey:
  def __init__(self, num, inventory, operation, test, test_true, test_false):
    self.num = num
    self.inventory = inventory
    self.operation = operation
    self.test = test
    self.test_true = test_true
    self.test_false = test_false
    self.inspected = 0

  def proceed(self):
    global total_test
    for item in self.inventory:
      self.inspected += 1
      item = self.multiply(item)
      #item = math.floor(item//3)
      item %= total_test
      if item % self.test == 0:
        monkeys[self.test_true].addItem(item)
      else:
        monkeys[self.test_false].addItem(item)
    self.inventory.clear()

  def multiply(self, item):
    op = self.operation.split(" ")
    if op[3] == "old":
      a = item
    else:
      a = int(op[3])
    if op[5] == "old":
      b = item
    else:
      b = int(op[5])
    if op[4] == "+":
      return a + b
    elif op[4] == "*":
      return a * b
    else:
      return a

  def addItem(self, item):
    self.inventory.append(item)



def main_a(filename):
  data = load_block(filename)
  monkeys.clear()
  for monkey in data:
    properties = monkey.split("\n")
    name = int(properties[0].split(" ")[1][:-1])
    inventory = [int(x) for x in properties[1].split(":")[1].split(",")]
    operation = properties[2].rstrip().split(":")[1]
    test = int(properties[3].rstrip().split(" ")[5])
    test_true = int(properties[4].rstrip().split(" ")[9])
    test_false = int(properties[5].rstrip().split(" ")[9])
    monkeys.append(Monkey(name, inventory, operation, test, test_true, test_false))
  for i in range(20):
    for monkey in monkeys:
      monkey.proceed()
  inspected = []
  for monkey in monkeys:
    inspected.append(monkey.inspected)
  inspected.sort()
  return inspected[-1]*inspected[-2]


def main_b(filename):
  data = load_block(filename)
  monkeys.clear()
  global total_test
  total_test = 1
  for monkey in data:
    properties = monkey.split("\n")
    name = int(properties[0].split(" ")[1][:-1])
    inventory = [int(x) for x in properties[1].split(":")[1].split(",")]
    operation = properties[2].rstrip().split(":")[1]
    test = int(properties[3].rstrip().split(" ")[5])
    total_test *= test
    test_true = int(properties[4].rstrip().split(" ")[9])
    test_false = int(properties[5].rstrip().split(" ")[9])
    monkeys.append(Monkey(name, inventory, operation, test, test_true, test_false))
  print(total_test)
  for i in range(10000):
    for monkey in monkeys:
      monkey.proceed()
  inspected = []
  for monkey in monkeys:
    inspected.append(monkey.inspected)
  inspected.sort()
  return inspected[-1]*inspected[-2]

    

#test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")


