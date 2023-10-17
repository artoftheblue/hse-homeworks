from sys import stdin
import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def __str__(self):
        return "\n".join("\t".join(str(item) for item in line) for line in self.matrix)

    def size(self):
        return (self.height, self.width)

exec(stdin.read())