import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np

FILE = "8.txt"
FILE_TEST = "8_test.txt"

def main_a(filename):
    data = lines(filename)
    suma = 0
    for line in data:
        l = line.rstrip().split(" | ")
        digits = l[0].split(" ")
        zadanie = l[1].split(" ")
        for z in zadanie:
            if (len(z) == 2 or len(z) == 3 or len(z) == 7 or len(z) == 4):
                suma += 1
    print(suma)

def main_b(filename):
    data = lines(filename)
    alph = ["a", "b", "c", "d", "e", "f", "g"]
    suma = 0
    for line in data:
        l = line.rstrip().split(" | ")
        digits = l[0].split(" ")
        zadanie = l[1].split(" ")
        digits_count = [0, 0, 0, 0, 0, 0, 0]
        correct_digits = ["z", "z", "z", "z", "z", "z", "z"]
        """
        In all ten digits together, segment "a" is there 8 times, "b" 6 times, "c" 8 times
        "d" 7 times, "e" 4 times, "f" 9 times and "g" 7 times. Thus we count how many times
        are individual elements in all digits and thanks to that we are able to decipher almost
        all digits. The two pairs which are not unambiguous are distinguished according whether
        they are in numbers 1 and 4
        """
        for d in digits:
            for i in d:
                digits_count[alph.index(i)] += 1
        for i in range(len(digits_count)):
            if (digits_count[i] == 4):
                correct_digits[i] = "e"
            if (digits_count[i] == 6):
                correct_digits[i] = "b"
            if (digits_count[i] == 7):
                for d in digits:
                    if (len(d) == 4):
                        if alph[i] in d:
                            correct_digits[i] = "d"
                        else:
                            correct_digits[i] = "g"
            if (digits_count[i] == 8):
                for d in digits:
                    if (len(d) == 2):
                        if alph[i] in d:
                            correct_digits[i] = "c"
                        else:
                            correct_digits[i] = "a"
            if (digits_count[i] == 9):
                correct_digits[i] = "f"

        result = 0
        for i in range(len(zadanie)):
            correct_number = []
            for d in zadanie[i]:
                correct_number.append(correct_digits[alph.index(d)])
            if (len(correct_number) == 2):
                result += pow(10,3-i) * 1
            if (len(correct_number) == 4):
                result += pow(10,3-i) * 4
            if (len(correct_number) == 3):
                result += pow(10,3-i) * 7
            if (len(correct_number) == 7):
                result += pow(10,3-i) * 8
            if (len(correct_number) == 6): #0 6 9
                if "d" not in correct_number:
                    result += pow(10,3-i) * 0
                if "c" not in correct_number:
                    result += pow(10,3-i) * 6
                if "e" not in correct_number:
                    result += pow(10,3-i) * 9
            if (len(correct_number) == 5): #2 3 5
                if "c" not in correct_number:
                    result += pow(10,3-i) * 5
                elif "f" not in correct_number:
                    result += pow(10,3-i) * 2
                else:
                    result += pow(10,3-i) * 3    
        suma += result
    print(suma)

main_a(FILE_TEST)
main_a(FILE)
main_b(FILE_TEST)
main_b(FILE)