class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f"{Matrix.__name__}:\n{self.matrix}"

    def __add__(self, other):
        """
        >>> print(m1 + m2)
        Matrix:
        [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        """
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
        """
        >>> m1 == m2
        True
        >>> m2 != m1
        False
        """
        return self.matrix == other.matrix

    def __gt__(self, other):
        """
        >>> Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]])) < m2
        False
        """
        return self.matrix > other.matrix

    def __lt__(self, other):
        """
        >>> m1 < Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]]))
        True
        """
        return self.matrix < other.matrix


if __name__ == '__main__':
    m1 = Matrix(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    m2 = Matrix(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    import doctest
    doctest.testmod(verbose=True)
