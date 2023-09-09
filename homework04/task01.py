'''
Напишите функцию для транспонирования матрицы.
'''


def transpose(mtrx):
    rows = len(mtrx)
    cols = len(mtrx[0])
    transposed = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = mtrx[i][j]
    return transposed


def print_matrix(matrix):
    for row in matrix:
        for elmt in row:
            print(elmt, end=" ")
        print()


my_matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
print_matrix(my_matrix)
print()
print_matrix(transpose(my_matrix))
