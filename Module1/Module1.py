from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import sys
import random
import math
import numpy as np


def get_edges(mtx):
    current_row = 0
    l_e = 0
    h_e = sys.maxsize
    for item in range(0, len(mtx)):
        for i in range(0, len(mtx[item])):
            current_row = item
            while current_row != len(mtx):
                for j in range(0, len(mtx[current_row])):
                    if i != j or current_row != item:
                        low = abs(mtx[item][i] - mtx[current_row][j])
                        high = abs(mtx[item][i] + mtx[current_row][j])
                        if low > l_e:
                            l_e = low
                        if high < h_e:
                            h_e = high
                current_row += 1
    return l_e, h_e


def user_input(low_edge, high_edge):
    user_num = int(input("Enter next number in range [" + str(low_edge) + ":" + str(high_edge) + "] "))
    while user_num < low_edge or user_num > high_edge:
        print("Wrong number, try again!")
        user_num = int(input("Enter next number in range [" + str(low_edge) + ":" + str(high_edge) + "] "))
    return user_num


def auto_fill():
    for item in range(1, mset):
        low_edge, high_edge = get_edges(matrix)
        random_number = random.randint(low_edge, high_edge)
        if len(matrix) != item:
            matrix[item].append(random_number)
        else:
            empty = []
            matrix.append(empty)
            matrix[item].append(random_number)
        while len(matrix[item]) != len(matrix[item - 1]) + 1:
            for element in range(1, len(matrix[item - 1]) + 1):
                low_edge, high_edge = get_edges(matrix)
                random_number = random.randint(low_edge, high_edge)
                matrix[item].append(random_number)
        print(matrix)
    single_list = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            single_list.append(
                matrix[i][j]
            )
    matrix_np = np.array(single_list)
    Z = linkage(matrix_np, 'ward')
    plt.figure(figsize=(25, 10))
    plt.title('Hierachical Clustering Dendrogram')
    plt.xlabel('sample matrix')
    plt.ylabel('distance')
    dendrogram(
                Z,
                leaf_rotation=90.,
                leaf_font_size=10,
    )
    plt.show()


def manual():
    for item in range(1, mset):
        low_edge, high_edge = get_edges(matrix)
        user_number = user_input(low_edge, high_edge)
        if len(matrix) != item:
            matrix[item].append(user_number)
        else:
            empty = []
            matrix.append(empty)
            matrix[item].append(user_number)
        while len(matrix[item]) != len(matrix[item - 1]) + 1:
            for element in range(1, len(matrix[item - 1]) + 1):
                low_edge, high_edge = get_edges(matrix)
                user_number = user_input(low_edge, high_edge)
                matrix[item].append(user_number)
        print(matrix)
    single_list = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            single_list.append(
                matrix[i][j]
            )
    matrix_np = np.array(single_list)
    Z = linkage(matrix_np, 'ward')
    plt.figure(figsize=(25, 10))
    plt.title('Hierachical Clustering Dendrogram')
    plt.xlabel('sample matrix')
    plt.ylabel('distance')
    dendrogram(
                Z,
                leaf_rotation=90.,
                leaf_font_size=10,
    )
    plt.show()


print("Welcome to matrix program!")
mset = int(input("Enter the number of elements for clusterization: "))
num1 = int(input("Please, enter first value: "))
print("Good.")
num2 = int(input("Enter second value: "))
choice = \
    input("Choose way to make metric space: 1 - manual filling metric table, 2 - auto fill, 3 - drop points on 2D plot")

matrix = [[],
          []]
matrix[0].append(num1)
matrix[1].append(num2)

fig, ax = plt.subplots()
ax.plot(100, 1, 100)

matrix_plot = []
tmp = [[], []]


def key_pressed(event):
    if event.key == 'enter':
        dist_matrix = build_matrix(tmp, matrix_plot)
        single_list = []
        for i in range(0, len(dist_matrix)):
            for j in range(0, len(dist_matrix[i])):
                single_list.append(
                    dist_matrix[i][j]
                )
        matrix_np = np.array(single_list)
        Z = linkage(matrix_np, 'single')
        plt.figure(figsize=(25, 10))
        plt.title('Hierachical Clustering Dendrogram')
        plt.xlabel('sample matrix')
        plt.ylabel('distance')
        dendrogram(Z,
                   truncate_mode='lastp',
                   p=12,
                   show_leaf_counts=True,
                   leaf_rotation=90.,
                   leaf_font_size=8,
                   show_contracted=True, )
        plt.show()
    else:
        print('Pressed not enter')


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


# restrict number of elements to add
def pick_up_point(event):
    if len(tmp) == 0:
        for i in range(0, 2):
            tmp.append([])
    x_point = event.xdata
    y_point = event.ydata
    print('picked: x = ' + str(x_point) + ', y = ' + str(y_point))
    tmp[0].append(x_point)
    tmp[1].append(y_point)
    plt.plot(tmp[0], tmp[1], 'ro')
    print(tmp)
    plt.show()


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))


# cid = fig.canvas.mpl_connect('button_press_event', onclick)

def make_plot():
    cid = fig.canvas.mpl_connect('button_press_event', pick_up_point)
    right_mouse = fig.canvas.mpl_connect('key_press_event', key_pressed)

    plt.show()


if choice == "1":
    manual()
elif choice == "2":
    auto_fill()
else:
    make_plot()
