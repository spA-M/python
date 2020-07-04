class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string = ''
        for i in self.matrix:
            for j in i:
                string += '%s\t' % j
            string = string[:-1]
            string += '\n'
        return string

    def __add__(self, other):

        string_1 = ''
        result = [[0, 0], [0, 0], [0, 0]]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        for r in result:
            for k in r:
                string_1 += '%s\t' % k
            string_1 = string_1[:-1]
            string_1 += '\n'
        return f"Суммарная матрица:\n{string_1}"


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 5], [2, 1], [9, 2]])

print(matrix_1)
print(matrix_2)
print(Matrix.__add__(matrix_1, matrix_2))