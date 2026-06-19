class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    if any(len(row) != matrix_length for row in matrix):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

    for row in matrix:
        for value in row:
            if not isinstance(value, int):
                raise MatrixContentError("The matrix must consist of only integers")

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()

    if not line:
        break

    try:
        row = [int(value) for value in line]
    except ValueError as error:
        raise MatrixContentError("The matrix must consist of only integers") from error

    mtrx.append(row)

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
