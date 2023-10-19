import sys
import numpy as np

def snake(M, N, direction="H"):
    result = np.arange(1, M * N + 1)
    if direction == "H":
        result = result.reshape(N, M)
        result[1::2] = result[1::2,::-1]
    else:
        result = result.reshape(M, N)
        result[::2] = result[::2,::-1]
        result = np.rot90(result)
    return result

print(snake(5, 3, "V"))
