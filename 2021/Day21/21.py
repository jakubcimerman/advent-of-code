import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime

DAY = datetime.date.today().day
test_exp_a = 739785
test_exp_b = 444356092776315


class Player:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.score = 0


    def move(self, value):
        self.pos = (self.pos + value - 1) % 10 + 1
        self.score += self.pos

    def addScore(self, score):
        self.score += score

    def returnScore(self):
        return self.score 


class Dice:
    def __init__(self):
        self.pos = 0
        self.tot_num_of_rolls = 0

    def roll(self):
        self.pos = (self.pos % 100) + 1
        self.tot_num_of_rolls += 1
        return self.pos

    def return_number_of_rolls(self):
        return self.tot_num_of_rolls


class QuantumDice:
    def __init__(self, p1, p2):
        results = []
        for x in range(1, 11):
            xline = []
            for y in range(1, 11):
                yline = []
                for i in range(31):
                    iline = []
                    for j in range(31):
                        jline = []
                        for b in range(2):
                            jline.append(0)
                        iline.append(jline)
                    yline.append(iline)
                xline.append(yline)
            results.append(xline)
        self.results = results
        self.results[p1][p2][0][0][0] += 1

    def roll(self):
        self.results
        for b in range(2):
            for i in range(21):
                for x in range(10):
                    for y in range(10):
                        for j in range(21):
                            for cube_x in range(1, 4):
                                for cube_y in range(1, 4):
                                    for cube_z in range(1, 4):
                                        add_value = cube_x + cube_y + cube_z
                                        #print((x + add_value) % 10, y, i+ (x+add_value)%10 + 1, j, 1-b)
                                        if b == 0:
                                            self.results[(x + add_value) % 10][y][i+ (x+add_value)%10 + 1][j][1-b] += self.results[x][y][i][j][b]
                                        else:
                                            self.results[x][(y + add_value) % 10][i][j + (y+add_value)%10 + 1][1-b] += self.results[x][y][i][j][b]
                            self.results[x][y][i][j][b] = 0


    def need_to_turn(self):
        r = self.results
        for x in range(10):
            for y in range(10):
                for i in range(21):
                    for j in range(21):
                        for b in range(2):
                            if r[x][y][i][j][b] > 0:
                                return True
        return False

    def result(self):
        r = self.results
        p1_wins = 0
        p2_wins = 0
        for x in range(10):
            for y in range(10):
                for i in range(21,31):
                    for j in range(0,21):
                        for b in range(2):
                            p1_wins += r[x][y][i][j][b]
                for j in range(21,31):
                    for i in range(0,21):
                        for b in range(2):
                            p2_wins += r[x][y][i][j][b]
        return [p1_wins, p2_wins]


def main_a(filename):
    data = lines(filename)
    p1 = Player(int(data[0]))
    p2 = Player(int(data[1]))
    c = Dice()
    p1Turn = True
    while p1.returnScore() < 1000 and p2.returnScore() < 1000:
        if p1Turn:
            p1.move(c.roll() + c.roll() + c.roll())
            p1Turn = False
        else:
            p2.move(c.roll() + c.roll() + c.roll())
            p1Turn = True
    print(p1.returnScore(), p2.returnScore())
    if p1.returnScore() >= 1000:
        return p2.returnScore() * c.return_number_of_rolls()
    else:
        return p1.returnScore() * c.return_number_of_rolls()


def main_b(filename):
    data = lines(filename)
    qc = QuantumDice(int(data[0]) - 1, int(data[1]) - 1)
    while qc.need_to_turn():
        qc.roll()
    result = qc.result()
    return(max(result))
    

test_and_submit(main_a, DAY, test_exp_a, "a")
test_and_submit(main_b, DAY, test_exp_b, "b")

