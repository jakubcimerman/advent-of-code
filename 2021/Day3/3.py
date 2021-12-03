import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np

FILE = "3.txt"
FILE_TEST = "3_test.txt"

def main_a(filename):
    eps = 0
    gamma = 0
    data = load_map_ll(filename)
    length = len(data[0])
    pozicia = np.empty(length)
    for line in data:
        for i in range(length):
            pozicia[i] += int(line[i])
    for i in range(length):
        if (pozicia[i] > len(data)*0.5):
            pozicia[i] = 1
        else:
            pozicia[i] = 0
    for i in range(length):
        gamma += pow(2,length-i-1)*pozicia[i]
        eps += pow(2, length -i-1)*(1-pozicia[i])
    print(gamma*eps)

def calc_gamma(data):
    gamma = 0
    length = len(data[0])
    pozicia = np.empty(length)
    old_array = data
    new_array = data
    for i in range(length):
        pozicia[i] = 0
        old_array = new_array
        new_array = []
        for line in old_array:
            pozicia[i] += int(line[i])
        if (pozicia[i] >= len(old_array)*0.5):
            pozicia[i] = 1
        else:
            pozicia[i] = 0
        for line in old_array:
            if (int(line[i]) == pozicia[i]):
                new_array.append(line)

    for i in range(length):
        gamma += pow(2,length-i-1)*pozicia[i]
    return(gamma)

def calc_eps(data):
    eps = 0
    length = len(data[0])
    pozicia = np.empty(length)
    old_array = data
    new_array = data
    for i in range(length):
        pozicia[i] = 0
        old_array = new_array
        new_array = []
        for line in old_array:
            pozicia[i] += int(line[i])
        if (pozicia[i] >= len(old_array)*0.5):
            pozicia[i] = 0
        else:
            pozicia[i] = 1
        for line in old_array:
            if (int(line[i]) == pozicia[i]):
                new_array.append(line)
        if (len(new_array)== 1):
            break

    for i in range(length):
        eps += pow(2,length-i-1)*int(new_array[0][i])
    return(eps)

def main_b(filename):
    """
    This code actually didn't work, so I did this part by simply ctrl+f in the input file and filtering the data myself,
    it was much faster than writing any code at all...
    After submitting the right answer I found the bug and made this part run
    """
    data = load_map_ll(filename)
    gamma = calc_gamma(data)
    eps = calc_eps(data)
    print(gamma*eps)

main_a(FILE_TEST)
main_a(FILE)
main_b(FILE_TEST)
main_b(FILE)
