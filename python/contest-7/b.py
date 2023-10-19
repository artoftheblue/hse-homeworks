import sys
import numpy as np
import numpy.linalg

def get_det_matrix(matrix):
    return np.linalg.det(matrix)

exec(sys.stdin.read())
