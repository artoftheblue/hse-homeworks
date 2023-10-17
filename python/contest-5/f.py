from sys import stdin
import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def __str__(self):
        return "\n".join("\t".join(str(item) for item in line) for line in self.matrix)

    def __add__(self, other):
        new = Matrix(self.matrix)
        for i in range(other.height):
            for j in range(other.width):
                new.matrix[i][j] += other.matrix[i][j]
        return new

    def __mul__(self, num):
        new = Matrix(self.matrix)
        for i in range(self.height):
            for j in range(self.width):
                new.matrix[i][j] *= num
        return new

    def __rmul__(self, num):
        return self * num

    def size(self):
        return (self.height, self.width)

exec(stdin.read())