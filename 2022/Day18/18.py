import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 64
test_exp_b = 58


def main_a(filename):
  data = lines(filename)
  cubes = []
  for line in data:
    cube = line.rstrip().split(",")
    cube = [int(x) for x in cube]
    cubes.append(cube)
  area = 0
  for cube in cubes:
    if [cube[0]+1, cube[1], cube[2]] not in cubes:
      area += 1
    if [cube[0]-1, cube[1], cube[2]] not in cubes:
      area += 1
    if [cube[0], cube[1]+1, cube[2]] not in cubes:
      area += 1
    if [cube[0], cube[1]-1, cube[2]] not in cubes:
      area += 1
    if [cube[0], cube[1], cube[2]+1] not in cubes:
      area += 1
    if [cube[0], cube[1], cube[2]-1] not in cubes:
      area += 1
  return area


def is_air_droplet(cubes, c):
  visited = []
  to_visit = [c]
  while len(to_visit) > 0:
    cube = to_visit[0]
    to_visit.pop(0)
    visited.append(cube)
    if max(cube) > max([max(x) for x in cubes]) or min(cube) < min([min(x) for x in cubes]):
      return []
    for neighbour in [
        [cube[0]+1, cube[1], cube[2]],
        [cube[0]-1, cube[1], cube[2]],
        [cube[0], cube[1]+1, cube[2]],
        [cube[0], cube[1]-1, cube[2]],
        [cube[0], cube[1], cube[2]+1],
        [cube[0], cube[1], cube[2]-1]
      ]:
      if neighbour not in cubes and neighbour not in visited and neighbour not in to_visit:
        to_visit.append(neighbour)
  return visited


def main_b(filename):
  data = lines(filename)
  cubes = []
  air_droplets = []
  for line in data:
    cube = line.rstrip().split(",")
    cube = [int(x) for x in cube]
    cubes.append(cube)
  area = 0
  for cube in cubes:
    for neighbour in [
      [cube[0]+1, cube[1], cube[2]],
      [cube[0]-1, cube[1], cube[2]],
      [cube[0], cube[1]+1, cube[2]],
      [cube[0], cube[1]-1, cube[2]],
      [cube[0], cube[1], cube[2]+1],
      [cube[0], cube[1], cube[2]-1]
    ]:
      if neighbour not in cubes and neighbour not in air_droplets:
        ad = is_air_droplet(cubes, neighbour)
        if ad == []:
          area += 1
        else:
          for c in ad:
            air_droplets.append(c) 
  return area


test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

