import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 2
test_exp_b = 4

def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def isLineSafe(nums):
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) > 3 or nums[i] == nums[i + 1] or sgn(nums[0] - nums[1]) * (nums[i] - nums[i + 1]) < 0:
            return False
    return True


def main_a(filename):
    data = lines(filename)
    safe_reports = 0
    for line in data:
        nums = [int(i) for i in line.split(" ")]
        if (isLineSafe(nums)):
            safe_reports += 1
    return safe_reports


def main_b(filename):
    data = lines(filename)
    safe_reports = 0
    for line in data:
        nums = [int(i) for i in line.split(" ")]
        if (isLineSafe(nums)):
            safe_reports += 1
        else:
            for i in range(len(nums)):
                new_nums = nums.copy()
                new_nums.pop(i)
                if (isLineSafe(new_nums)):
                    safe_reports += 1
                    break
    return safe_reports

    
test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

