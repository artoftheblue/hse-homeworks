import sys
import numpy as np

def multiplication_matrix(size):
    line = np.arange(1, size + 1)
    array = np.array([line * i for i in range(1, size + 1)])
    array.resize(size, size)
    return array
    
exec(sys.stdin.read())
