class Solution:
    def countSpanTree(self, n, edges):
        # Create Laplacian Matrix
        lap = [[0] * n for _ in range(n)]

        for u, v in edges:
            lap[u][u] += 1
            lap[v][v] += 1
            lap[u][v] -= 1
            lap[v][u] -= 1

        # Remove last row and column to form cofactor matrix
        mat = [row[:-1] for row in lap[:-1]]

        # Function to find determinant using Gaussian Elimination
        def determinant(matrix):
            size = len(matrix)
            det = 1

            for i in range(size):
                pivot = i

                while pivot < size and matrix[pivot][i] == 0:
                    pivot += 1

                if pivot == size:
                    return 0

                if pivot != i:
                    matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
                    det *= -1

                det *= matrix[i][i]

                for j in range(i + 1, size):
                    factor = matrix[j][i] / matrix[i][i]

                    for k in range(i, size):
                        matrix[j][k] -= factor * matrix[i][k]

            return round(det)

        return determinant(mat)
