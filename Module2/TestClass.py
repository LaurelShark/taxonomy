import math

points_array = [[21.16935483870968, 22.721774193548384, 78.60887096774192, 40.685483870967744],
                [87.74285714285716, 17.323214285714293, 36.76964285714287, 16.144642857142863]]

matrix = []


def fill_cell(row, column, arr, matr):
    # row = 1
    # column = 0
    matr[row][column] = math.sqrt(
        (arr[0][column] - arr[0][row + 1]) ** 2 + (arr[1][column] - arr[1][row + 1]) ** 2
    )
    return matr[row][column]


def build_matrix(coord_array, mtx):
    mtx_depth = len(coord_array[0]) - 1
    for i in range(0, mtx_depth):
        mtx.append([0])
        for j in range(0, i):
            mtx[i].append(0)
    # print(mtx[1][0])
    row_length = 1
    for item in range(0, mtx_depth):
        for i in range(0, row_length):
            mtx[item][i] = fill_cell(item, i, coord_array, mtx)
        row_length += 1
    print(mtx)
    return mtx


build_matrix(points_array, matrix)

