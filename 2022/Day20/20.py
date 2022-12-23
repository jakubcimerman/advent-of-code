import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = 20
test_exp_a = 3
test_exp_b = 1623178306

class Number:
  def __init__(self, n):
    self.n = n
    self.r = None
    self.l = None

  def set_right(self, r):
    self.r = r

  def set_left(self, l):
    self.l = l

def sgn(x):
  if x > 0:
    return 1
  if x < 0:
    return -1
  return 0

def print_nums(nums):
  to_print = ""
  n = nums[0]
  for i in range(len(nums)):
    print(nums[i].l.n, nums[i].n, nums[i].r.n)
    #to_print += str(n.n) + ", "
    #n = n.r
  print(to_print)

def main_a(filename):
  data = lines(filename)
  data = [int(x.strip()) for x in data]
  N = len(data)
  nums = []
  for i in range(len(data)):
    nums.append(Number(data[i]))
  for i in range(len(data)):
    nums[i].set_right(nums[(i+1)%N])
    nums[i].set_left(nums[(i-1)%N])
  for i in range(N):
    for x in range(abs(nums[i].n)):
      if nums[i].n > 0:
        a = nums[i].l
        b = nums[i]
        c = nums[i].r
        d = nums[i].r.r
        nums[i].r.set_left(a)
        nums[i].l.set_right(c)
        nums[i].r.r.set_left(b)
        nums[i].r.set_right(b)
        nums[i].set_right(d)
        nums[i].set_left(c)
      if nums[i].n < 0:
        a = nums[i].l.l
        b = nums[i].l
        c = nums[i]
        d = nums[i].r
        nums[i].l.set_right(d)
        nums[i].r.set_left(b)
        nums[i].l.l.set_right(c)
        nums[i].l.set_left(c)
        nums[i].set_left(a)
        nums[i].set_right(b)
  result = 0
  grove = []
  for i in range(N):
    if nums[i].n == 0:
      n = nums[i]
      for x in range(3):
        for y in range(1000):
          n = n.r
        grove.append(n.n)
        result += n.n
      break
  return result

def main_b(filename):
  data = lines(filename)
  data = [int(x.strip()) for x in data]
  N = len(data)
  nums = []
  for i in range(len(data)):
    nums.append(Number(data[i]*811589153))
  for i in range(len(data)):
    nums[i].set_right(nums[(i+1)%N])
    nums[i].set_left(nums[(i-1)%N])
  for t in range(10):
    for i in range(N):
      if nums[i].n > 0:
        add = nums[i].n % (N-1)
      else:
        add = - ((-nums[i].n) % (N-1))
      for x in range(abs(add)):
        if nums[i].n > 0:
          a = nums[i].l
          b = nums[i]
          c = nums[i].r
          d = nums[i].r.r
          nums[i].r.set_left(a)
          nums[i].l.set_right(c)
          nums[i].r.r.set_left(b)
          nums[i].r.set_right(b)
          nums[i].set_right(d)
          nums[i].set_left(c)
        if nums[i].n < 0:
          a = nums[i].l.l
          b = nums[i].l
          c = nums[i]
          d = nums[i].r
          nums[i].l.set_right(d)
          nums[i].r.set_left(b)
          nums[i].l.l.set_right(c)
          nums[i].l.set_left(c)
          nums[i].set_left(a)
          nums[i].set_right(b)
  result = 0
  grove = []
  for i in range(N):
    if nums[i].n == 0:
      n = nums[i]
      for x in range(3):
        for y in range(1000):
          n = n.r
        grove.append(n.n)
        result += n.n
      break
  return result



test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")
