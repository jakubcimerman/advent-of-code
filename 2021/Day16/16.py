import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
from collections import Counter

DAY = datetime.date.today().day
test_exp_a = 31
test_exp_b = 0


hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
bina = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]


def literal_value(bin_mes, pos):
    numbers = []
    bin_pos = pos
    new_binary_number = ""
    while bin_mes[bin_pos] == "1":
        bin_pos += 1
        for i in range(4):
            new_binary_number += bin_mes[bin_pos]
            bin_pos += 1
    bin_pos += 1
    for i in range(4):
        new_binary_number += bin_mes[bin_pos]
        bin_pos += 1
    number = 0
    for i in range(len(new_binary_number)):
        number += int(new_binary_number[i]) * pow(2, len(new_binary_number) - 1 - i)
    return [bin_pos, number]


def product(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def read_packet(bin_mes, pos):
    version = 0
    total_version = 0
    bin_pos = pos
    for i in range(3):
        version += int(bin_mes[bin_pos])*pow(2,2-i)
        bin_pos += 1
    total_version += version
    typeID = 0
    for i in range(3):
        typeID += int(bin_mes[bin_pos])*pow(2,2-i)
        bin_pos += 1

    if typeID == 4:
        p, numbers = literal_value(bin_mes, bin_pos)
        bin_pos = p
        return [bin_pos, total_version, numbers]
    else:
        ltID = bin_mes[bin_pos]
        bin_pos += 1
        numbers = []
        if ltID == "0":
            length_in_bits = 0
            for i in range(15):
                length_in_bits += int(bin_mes[bin_pos]) * pow(2, 14 - i)
                bitsToDO = bin_pos + length_in_bits
                bin_pos += 1
            while bin_pos <= bitsToDO:
                [p, ver, v] = read_packet(bin_mes, bin_pos)
                bin_pos = p
                total_version += ver
                if isinstance(v,list):
                    for n in v:
                        numbers.append(n)
                else:
                    numbers.append(v)
        if ltID == "1":
            num_of_subpackets = 0
            for i in range(11):
                num_of_subpackets += int(bin_mes[bin_pos]) * pow(2, 10 - i)
                bin_pos += 1
            for i in range(num_of_subpackets):
                [p, ver, v] = read_packet(bin_mes, bin_pos)
                bin_pos = p
                total_version += ver
                if isinstance(v,list):
                    for n in v:
                        numbers.append(n)
                else:
                    numbers.append(v)
        if typeID == 0:
            return [bin_pos, total_version, sum(numbers)]
        if typeID == 1:
            return [bin_pos, total_version, product(numbers)]
        if typeID == 2:
            return [bin_pos, total_version, min(numbers)]
        if typeID == 3:
            return [bin_pos, total_version, max(numbers)]
        if typeID == 5:
            return [bin_pos, total_version, numbers[0] > numbers[1]]
        if typeID == 6:
            return [bin_pos, total_version, numbers[0] < numbers[1]]
        if typeID == 7:
            return [bin_pos, total_version, numbers[0] == numbers[1]]


def main_a(filename):
    data = lines(filename)
    for line in data:
        line = line.rstrip()
        bin_mes = ""
        bin_pos = 0
        for i in range(len(line)):
            bin_mes += bina[hexa.index(line[i])]
        b, ver, v = read_packet(bin_mes, 0) 
        print("version", ver)
        print("answer", v)
    return 


main_a("16_test.txt")
main_a("16.txt")