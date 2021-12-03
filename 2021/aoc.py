import numpy as np

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