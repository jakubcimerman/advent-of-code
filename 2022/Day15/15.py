import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 26
test_exp_b = 56000011

def dist_of_points(A, B):
  return abs(A[0]-B[0])+abs(A[1]-B[1])

def dist_from_line(A, y):
  return abs(A[1]-y)

def between(x, A, B):
  if x >= A and x <= B:
    return True
  return False

def switch(A):
  temp = A[0]
  A[0] = A[-1]
  A[-1] = temp

def beacons_in_range(beacons, range, y):
  beacs = []
  for b in beacons:
    if b[1] == y and between(b[0], range[0], range[1]):
      if b not in beacs:
        beacs.append(b)
  return(len(beacs))

def main_a(filename):
  if filename == "15.txt":
    studied_y = 2000000
  else:
    studied_y = 10
  data = lines(filename)
  sensors = []
  beacons = []
  for line in data:
    line = line.split(":")
    sensor = line[0].split(",")
    sensor = [int(x.split("=")[1]) for x in sensor]
    closest_beacon = line[1].split(",")
    closest_beacon = [int(x.split("=")[1]) for x in closest_beacon]
    sensors.append(sensor)
    beacons.append(closest_beacon)
  possible_beacons = []
  for i in range(len(sensors)):
    d1 = dist_of_points(sensors[i], beacons[i])
    d2 = dist_from_line(sensors[i], studied_y)
    d = d1 - d2
    if d > 0:
      possible_beacons.append([sensors[i][0]-d, sensors[i][0]+d])
  while len(possible_beacons) > 1:
    for i in range(1, len(possible_beacons)):
      if between(possible_beacons[i][0], possible_beacons[0][0], possible_beacons[0][1]) and possible_beacons[i][1] > possible_beacons[0][1]:
        possible_beacons[0][1] = possible_beacons[i][1]
        possible_beacons.pop(i)
        break
      if between(possible_beacons[i][1], possible_beacons[0][0], possible_beacons[0][1]) and possible_beacons[i][0] < possible_beacons[0][0]:
        possible_beacons[0][0] = possible_beacons[i][0]
        possible_beacons.pop(i)
        break
      if between(possible_beacons[i][0], possible_beacons[0][0], possible_beacons[0][1]) and between(possible_beacons[i][1], possible_beacons[0][0], possible_beacons[0][1]):
        possible_beacons.pop(i)
        break
      if possible_beacons[i][0] < possible_beacons[0][0] and possible_beacons[i][1] > possible_beacons[0][1]:
        possible_beacons[0][0] = possible_beacons[i][0]
        possible_beacons[0][1] = possible_beacons[i][1]
        possible_beacons.pop()
        break
  return possible_beacons[0][1] - possible_beacons[0][0] + 1 - beacons_in_range(beacons, possible_beacons[0], studied_y)



def main_b(filename):
  if filename == "15.txt":
    max_range = 4000000
    min_range = 3000000
  else:
    max_range = 20
    min_range = 0
  data = lines(filename)
  sensors = []
  beacons = []
  for line in data:
    line = line.split(":")
    sensor = line[0].split(",")
    sensor = [int(x.split("=")[1]) for x in sensor]
    closest_beacon = line[1].split(",")
    closest_beacon = [int(x.split("=")[1]) for x in closest_beacon]
    sensors.append(sensor)
    beacons.append(closest_beacon)
  for y in range(min_range, max_range+1):
    possible_beacons = []
    for i in range(len(sensors)):
      d1 = dist_of_points(sensors[i], beacons[i])
      d2 = dist_from_line(sensors[i], y)
      d = d1 - d2
      if d > 0:
        possible_beacons.append([sensors[i][0]-d, sensors[i][0]+d])
    num_of_cycles = 0
    while len(possible_beacons) > 1:
      num_of_cycles += 1
      for i in range(1, len(possible_beacons)):
        if between(possible_beacons[i][0], possible_beacons[0][0]-1, possible_beacons[0][1]+1) and possible_beacons[i][1] > possible_beacons[0][1]:
          possible_beacons[0][1] = possible_beacons[i][1]
          possible_beacons.pop(i)
          break
        if between(possible_beacons[i][1], possible_beacons[0][0]-1, possible_beacons[0][1]+1) and possible_beacons[i][0] < possible_beacons[0][0]:
          possible_beacons[0][0] = possible_beacons[i][0]
          possible_beacons.pop(i)
          break
        if between(possible_beacons[i][0], possible_beacons[0][0]-1, possible_beacons[0][1]+1) and between(possible_beacons[i][1], possible_beacons[0][0], possible_beacons[0][1]):
          possible_beacons.pop(i)
          break
        if possible_beacons[i][0] < possible_beacons[0][0] and possible_beacons[i][1] > possible_beacons[0][1]:
          possible_beacons[0][0] = possible_beacons[i][0]
          possible_beacons[0][1] = possible_beacons[i][1]
          possible_beacons.pop()
          break
      if num_of_cycles > len(sensors) + 5:
        if len(possible_beacons) > 3:
          switch(possible_beacons)
          num_of_cycles = 0
        else:
          return y + 4000000 * (possible_beacons[0][1]+1)
          break
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")


