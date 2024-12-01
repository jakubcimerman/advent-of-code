import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 11
test_exp_b = 31


def main_a(filename):
    data = load_numpy_data(filename)
    data[0].sort()
    data[1].sort()
    result = 0
    for i in range(len(data[0])):
    	result += abs(data[0][i] - data[1][i])
    return int(result)


def main_b(filename):
    data = load_numpy_data(filename)
    result = 0
    for i in range(len(data[0])):
    	result += (data[1] == data[0][i]).sum() * data[0][i]
    return int(result)
    
# test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

