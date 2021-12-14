import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
from collections import Counter

DAY = datetime.date.today().day
test_exp_a = 1588
test_exp_b = 2188189693529


def main_a(filename):
    steps = 10
    data = file(filename)
    data = data.split("\n\n")
    dna = data[0].rstrip()
    instructions = data[1].split("\n")
    inst = []
    for line in instructions:
        x,y = line.split(" -> ")
        inst.append([x,y])

    for s in range(steps):
        new_dna = ""
        for i in range(len(dna)-1):
            for instruction in inst:
                if dna[i:i+2] in instruction[0]:
                    new_dna += dna[i:i+1]
                    new_dna += instruction[1]
        new_dna += dna[-1]
        dna = new_dna
    c = Counter(dna)
    return c.most_common(len(c))[0][1] - c.most_common(len(c))[-1][1]
    


def main_b(filename):
    steps = 39
    data = file(filename)
    data = data.split("\n\n")
    dna = data[0].rstrip()
    instructions = data[1].split("\n")
    inst_x = []
    inst_y = []
    count_inst = []
    for line in instructions:
        x,y = line.split(" -> ")
        inst_x.append(x)
        inst_y.append(y)
        count_inst.append(0)
    alphabet = []
    count_alph = []
    for a in dna:
        if a not in alphabet:
            alphabet.append(a)
            count_alph.append(0)
    for a in inst_y:
        if a not in alphabet:
            alphabet.append(a)
            count_alph.append(0)
    for i in range(len(dna)-1):
        for j in range(len(inst_x)):
            if dna[i:i+2] in inst_x[j]:
                count_inst[j] += 1
    for s in range(steps):
        ci = count_inst.copy()
        for i in range(len(count_inst)):
            x = inst_x[i]
            y = inst_y[i]
            ci[i] -= count_inst[i]
            ci[inst_x.index(inst_x[i][0] + inst_y[i])] += count_inst[i]
            ci[inst_x.index(inst_y[i] + inst_x[i][1])] += count_inst[i]
        count_inst = ci.copy()

    for i in range(len(count_inst)):
        count_alph[alphabet.index(inst_x[i][0])] += count_inst[i]
        count_alph[alphabet.index(inst_y[i])] += count_inst[i]
    count_alph[alphabet.index(dna[-1])] += 1
    return max(count_alph) - min(count_alph)
    

#est_and_submit(main_a, DAY, test_exp_a, "a")
#test_and_submit(main_b, DAY, test_exp_b, "b")

print(main_a("14_test.txt"))
print(main_a("14.txt"))
print(main_b("14_test.txt"))
print(main_b("14.txt"))
