import sys
import numpy as np

def manhattan_distance(a, b):
    return np.sum(np.abs(a - b)).astype("int32")

exec(sys.stdin.read())
