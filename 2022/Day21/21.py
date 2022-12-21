import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 152
test_exp_b = 301

monkeys = {}

class Monkey:
  def __init__(self, name, command):
    self.name = name
    if command.isdigit():
      self.type = "num"
      self.num = int(command)
    else:
      parts = command.split(" ")
      self.type = "operation"
      self.A = parts[0]
      self.B = parts[2]
      self.operation = parts[1]

  def find_human(self):
    if self.name == "humn":
      self.is_human_in_branch = True
      return self.is_human_in_branch
    if self.type == "num":
      self.is_human_in_branch = False
      return self.is_human_in_branch
    self.is_human_in_branch = monkeys[self.A].find_human() or monkeys[self.B].find_human()
    return self.is_human_in_branch

  def set_num(self, num):
    self.num = num

  def yell(self):
    if self.type == "num":
      return self.num
    else:
      if self.operation == "+":
        return monkeys[self.A].yell() + monkeys[self.B].yell()
      if self.operation == "-":
        return monkeys[self.A].yell() - monkeys[self.B].yell()
      if self.operation == "*":
        return monkeys[self.A].yell() * monkeys[self.B].yell()
      if self.operation == "/":
        return monkeys[self.A].yell() / monkeys[self.B].yell()
      if self.operation == "=":
        return monkeys[self.A].yell() == monkeys[self.B].yell()

  def reverse(self, num):
    if self.name == "humn":
      return num
    if self.name == "root":
      if monkeys[self.A].find_human():
        return monkeys[self.A].reverse(monkeys[self.B].yell())
      else:
        return monkeys[self.B].reverse(monkeys[self.A].yell())
    if monkeys[self.A].find_human():
      if self.operation == "+":
        return monkeys[self.A].reverse(num-monkeys[self.B].yell())
      if self.operation == "-":
        return monkeys[self.A].reverse(num+monkeys[self.B].yell())
      if self.operation == "*":
        return monkeys[self.A].reverse(num/monkeys[self.B].yell())
      if self.operation == "/":
        return monkeys[self.A].reverse(num*monkeys[self.B].yell())
    else:
      if self.operation == "+":
        return monkeys[self.B].reverse(num-monkeys[self.A].yell())
      if self.operation == "-":
        return monkeys[self.B].reverse(-num+monkeys[self.A].yell())
      if self.operation == "*":
        return monkeys[self.B].reverse(num/monkeys[self.A].yell())
      if self.operation == "/":
        return monkeys[self.B].reverse(monkeys[self.A].yell()/num)

def main_a(filename):
  data = lines(filename)
  monkeys.clear()
  for l in data:
    name, command = l.rstrip().split(": ")
    monkeys[name] = Monkey(name, command)
  return int(monkeys["root"].yell())

def main_b(filename):
  data = lines(filename)
  monkeys.clear()
  for l in data:
    name, command = l.rstrip().split(": ")
    if name == "root":
      command = command.replace("+", "=")
    monkeys[name] = Monkey(name, command)
  for m in monkeys:
    monkeys[m].find_human()
  return int(monkeys["root"].reverse(0))


test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")
