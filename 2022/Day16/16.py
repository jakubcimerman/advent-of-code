import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
import math
import json

DAY = datetime.date.today().day
test_exp_a = 1651
test_exp_b = 1707


def calculate_distances(valves, A, B, distance, visited):
  v = visited.copy()
  v.append(A)
  if A == B:
    return distance
  elif B in valves[A]["tunnels"]:
    return distance + 1
  else:
    min_dist = 1000
    for t in valves[A]["tunnels"]:
      if t not in v:
        d = calculate_distances(valves, t, B, distance + 1, v)
        if d < min_dist:
          min_dist = d
    return min_dist

def best_path(valves, A, total_pressure, remaining_time, visited):
  if remaining_time <= 0:
    return 0
  v = visited.copy()
  v.append(A)
  best_option = 0
  best_next_pos = 0
  for B, dist in valves[A]["distances"].items():
    if B not in v and B != A and valves[B]["flowrate"] > 0:
      pressure = best_path(valves, B, valves[B]["flowrate"] * (remaining_time - 1 - dist), remaining_time - 1 - dist, v)
      if pressure > best_option:
        best_option = pressure
        best_next_pos = B
  return total_pressure + best_option

def best_path_b(valves, p, A, total_pressure, o):
  if p[0][1] <= 0 or p[1][1] <= 0:
    return 0
  if len(o) >= len(valves["AA"]["distances"]) + 1:
    return 0
  if total_pressure < 0:
    return 0
  opened = o.copy()
  opened.append(A)
  players = p.copy()
  best_option = 0
  best_next_pos = 0
  best_next_pres = 0
  for B, dist in valves[players[0][0]]["distances"].items():
    if B not in opened:
      next_pres = valves[B]["flowrate"] * (players[0][1] - 1 - dist)
      if next_pres > 0.7*best_next_pres:
        if next_pres > best_next_pres:
          best_next_pres = next_pres
        pressure = best_path_b(valves, [[B, players[0][1] - 1 - dist], players[1]], B, next_pres, opened)
        if pressure >= best_option:
          best_option = pressure
          best_next_pos = B
          p = 0
  for B, dist in valves[players[1][0]]["distances"].items():
    if B not in opened:
      next_pres = valves[B]["flowrate"] * (players[1][1] - 1 - dist)
      if next_pres > 0.7*best_next_pres:
        if next_pres > best_next_pres:
          best_next_pres = next_pres
        pressure = best_path_b(valves, [players[0], [B, players[1][1] - 1 - dist]], B, next_pres, opened)
        if pressure >= best_option:
          best_option = pressure
          best_next_pos = B
          p = 1
  return total_pressure + best_option


def main_a(filename):
  data = lines(filename)
  valves = {}
  for l in data:
    name = l.split(" ")[1]
    flowrate = int(l.split(";")[0].split("=")[1])
    tunnels = l.split("to valve")[1].rstrip()
    if tunnels [0] == "s":
      tunnels = tunnels[2:].split(", ")
    else:
      tunnels = [tunnels[1:]]
    valves[name] = {
      "flowrate": flowrate,
      "tunnels": tunnels
    }
  for A in valves:
    valves[A]["distances"] = {}
    for B in valves:
      if valves[B]["flowrate"] > 0:
        valves[A]["distances"][B] = calculate_distances(valves, A, B, 0, [])
  return best_path(valves, "AA", 0, 30, [])


def main_b(filename):
  data = lines(filename)
  valves = {}
  for l in data:
    name = l.split(" ")[1]
    flowrate = int(l.split(";")[0].split("=")[1])
    tunnels = l.split("to valve")[1].rstrip()
    if tunnels [0] == "s":
      tunnels = tunnels[2:].split(", ")
    else:
      tunnels = [tunnels[1:]]
    valves[name] = {
      "flowrate": flowrate,
      "tunnels": tunnels
    }
  for A in valves:
    valves[A]["distances"] = {}
    for B in valves:
      if valves[B]["flowrate"] > 0:
        valves[A]["distances"][B] = calculate_distances(valves, A, B, 0, [])
  players = [["AA", 26], ["AA", 26]]
  opened = []
  total_pressure = 0
  return best_path_b(valves, players, "AA", 0, [])
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

