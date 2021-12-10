import numpy as np
from aocd import submit


def lines(path):
    """
    Return a list of lines from the file `path`
    """
    with open(path) as f:
        return f.readlines()


def file(path: str) -> str:
    """
    Return contents of a file at `path` as a string
    """
    with open(path) as f:
        return f.read()


def load_block(path):
    """
    Return a list of blocks from file separated by empty line
    """
    return file(path).split("\n\n")


def filerstrip(path: str) -> str:
    """
    Return rstripped file contents of file at `path`
    """
    return file(path).rstrip()


def load_map_ll(path):
    """Return list of lists of one char strings ("2D array") from the file at
    `path`
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: list(x.rstrip()), lines))


def load_ints_split(path, splitchar):
    """
    Return a list of ints loaded from file at `path` delimited by splitchar.
    """
    line = file(path)
    return [int(i) for i in line.split(splitchar)]


def load_strings_split(path, splitchar):
    """
    Return a list of strings loaded from file at `path` delimited by splitchar.
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: x.split(splitchar), lines))


def load_numpy_data(path):
    """
    Return ndarray of floats loaded from file at `path`
    """
    return np.loadtxt(path, unpack=True)


def convert_base(num, from_base, to_base):
    """
    Convert base of a number in string format
    """
    dec = 0
    for i in range(len(num)):
        dec += pow(from_base,length-i-1)*int(num[i])
    if dec == 0:
        return "0"
    if to_base == 10:
        return str(dec)
    result = ""
    while dec:
        result += str(int(dec % to_base))
        dec //= to_base
    return result[::-1]


def test_and_submit(f, day, exp, part):
    """
    Run the code for test input, compare it with expected result and if correct, submit
    """
    FILENAME = f"{day}.txt"
    FILENAME_TEST = f"{day}_test.txt"
    obtained = f(FILENAME_TEST)
    print(obtained, exp)
    if (str(obtained).rstrip() != str(exp).rstrip()):
        print("Value obtained from test input is not equal to the expected value")
        return
    result = f(FILENAME)
    print("Submitting result: ", result)
    submit(result, part=part, day=day, year=2021)


def add_array_border(data, border):
    """
    Add line and column of custom chars/ints/strings to the all four borders of 2D array
    Thus when checking for neighbouring elements in the all directions, one can avoid writing lots of ifs
    """
    result = []
    for i in range(len(data)+2):
        line = []
        for j in range(len(data[0])+2):
            if (j == 0 or i == 0 or i == len(data)+1 or j == len(data[0])+1):
                line.append(border)
            else:
                line.append(data[i-1][j-1])
        result.append(line)
    return result
