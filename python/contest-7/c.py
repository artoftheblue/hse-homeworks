import sys
import numpy as np

def make_board(size):
    matrix = np.zeros((size, size), dtype=int)

    matrix[::2, ::2], matrix[1::2, 1::2] = 1, 1
    return matrix

exec(sys.stdin.read())
