class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f"{Matrix.__name__}:\n{self.matrix}"

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            result = []
            temp = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    sum_matrix = other.matrix[i][j] + self.matrix[i][j]
                    temp.append(sum_matrix)
                    if len(temp) == len(self.matrix[0]):
                        result.append(temp)
                        temp = []
            return Matrix(matrix=result)
        else:
            return f'Матрицы разного размера'

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __gt__(self, other):
        return self.matrix > other.matrix

    def __lt__(self, other):
        return self.matrix < other.matrix
