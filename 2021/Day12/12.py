import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
from functools import lru_cache

DAY = datetime.date.today().day
test_exp_a = 226
test_exp_b = 3509

#@lru_cache
def find_path(data, starting_point, _visited):
    visited = _visited.copy()
    if (starting_point == "end"):
        return 1
    else:
        pathes = 0
        for l in data:
            for i in range(2):
                if (starting_point == l[i] and l[i-1] not in visited):
                    if (starting_point.isupper()):
                        pathes += find_path(data, l[1-i], visited)
                    else:
                        visited.append(starting_point)
                        pathes += find_path(data, l[1-i], visited)
        return pathes  



def main_a(filename):
    data = load_strings_split(filename, "-")
    for i in range(len(data)):
        data[i][1] = data[i][1].rstrip()
    pathes = find_path(data, "start", [])
    return pathes


def find_path_b(data, starting_point, _visited_once, _visited_twice):
    if (starting_point == "end"):
        return 1
    else:
        pathes = 0
        for l in data:
            for i in range(2):
                if (starting_point == l[i] and ((l[i-1] not in _visited_twice and len(_visited_twice) < 2 and starting_point not in _visited_once) or (l[i-1] not in _visited_once))):
                    visited_once = _visited_once.copy()
                    visited_twice = _visited_twice.copy()
                    if (starting_point.isupper()):
                        pathes += find_path_b(data, l[1-i], visited_once, visited_twice)
                    else:
                        if (starting_point in visited_once):
                            visited_twice.append(starting_point)
                        else:
                            visited_once.append(starting_point)
                        pathes += find_path_b(data, l[1-i], visited_once, visited_twice)
        return pathes  



def main_b(filename):
    data = load_strings_split(filename, "-")
    for i in range(len(data)):
        data[i][1] = data[i][1].rstrip()
    pathes = find_path_b(data, "start", ["start"], [])
    return pathes

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

