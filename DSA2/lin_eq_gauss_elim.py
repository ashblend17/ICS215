def gauss_jordan_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]
    solutions = [row[-1] for row in matrix]
    return solutions
matrix = [
    [1, 1, 1, 2],
    [2, 3, 1, 3],
    [1, -1, -2, -6]
]
solutions = gauss_jordan_elimination(matrix)
print("Solutions:")
print("x=",int(solutions[0]),"y=",int(solutions[1]),"z=",int(solutions[2]))