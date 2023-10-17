from sys import stdin
import copy

class MatrixError(Exception):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def __str__(self):
        return "\n".join("\t".join(str(item) for item in line) for line in self.matrix)

    def __add__(self, other):
        if self.height != other.height or self.width != other.width:
            raise MatrixError(self, other)
            
        new = Matrix(self.matrix)
        for i in range(other.height):
            for j in range(other.width):
                new.matrix[i][j] += other.matrix[i][j]
        return new

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new = [[0 for k in range(self.width)] for m in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    new[i][j] = self.matrix[i][j] * other
            return Matrix(new)
        elif isinstance(other, Matrix):
            if self.width != other.height:
                raise MatrixError(self, other)
            
            new = [[0 for k in range(other.width)] for m in range(self.height)]
            for i in range(self.height):
                for j in range(other.width):
                    new[i][j] = sum(map(lambda x: x[0] * x[1], zip(self.matrix[i], (other.matrix[z][j] for z in range(other.height)))))
            return Matrix(new)
        else:
            raise ValueError

    def __rmul__(self, other):
        return self * other

    def transpose(self):
        new = [[0 for k in range(self.height)] for m in range(self.width)]
        for i in range(self.width):
            for j in range(self.height):
                new[i][j] = self.matrix[j][i]
        self.matrix = new
        self.width, self.height = self.height, self.width
        return self

    @staticmethod
    def transposed(matrix):
        new = Matrix([[0 for _ in range(matrix.height)] for _ in range(matrix.width)])
        for i in range(matrix.width):
            for j in range(matrix.height):
                new.matrix[i][j] = matrix.matrix[j][i]
        return new

    def size(self):
        return (self.height, self.width)

exec(stdin.read())