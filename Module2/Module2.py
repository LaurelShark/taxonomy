import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()
ax.plot(100, 1, 100)

matrix = []
tmp = [[], []]
mset = int(input('Enter the number of elements: '))
counter = 0


def compute_distances(arr):
    distance = math.sqrt((arr[0][0] - arr[0][1]) ** 2 + (arr[1][0] - arr[1][1]) ** 2)
    return distance


def key_pressed(event):
    if event.key == 'enter':
        build_matrix(tmp, matrix)
    else:
        print('Pressed not enter')


def build_matrix(data_array, mtx):
    #print(str(data_array[0][0]) + "; " + str(data_array[0][1]))
    #print(str(data_array[1][0]) + "; " + str(data_array[1][1]))
    mtx_depth = len(data_array[0]) - 1
    for i in range(0, mtx_depth):
        mtx.append([0])
        for j in range(0, i):
            mtx[i].append(0)
    print(mtx[1][0])
    row_length = 1
    for item in range(0, mtx_depth):
        for i in range(0, row_length):
            for j in range(1, row_length + 1):
                if j < len(data_array[0]):
                    mtx[item][i] = math.sqrt((data_array[i][i] - data_array[i][j]) ** 2 +
                                             (data_array[j][i] - data_array[j][j]) ** 2)
        row_length += 1
    print(mtx)
    return mtx


# build matrix from tmp array
def build_matrix_old(arr, mtx):
    print('here')
    if len(mtx) < len(arr[0]):
        mtx.append([])
        print(mtx)
    for item in range(0, len(mtx) - 1):
        for i in range(0, len(arr[0]) - 1):
            for j in range(1, len(arr[1])):
                mtx[item][i] = math.sqrt((arr[i][i] - arr[i][j]) ** 2 + (arr[j][i] - arr[j][j]) ** 2)
                print(mtx[item][i])
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
    print(tmp)


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))


# cid = fig.canvas.mpl_connect('button_press_event', onclick)

cid = fig.canvas.mpl_connect('button_press_event', pick_up_point)
right_mouse = fig.canvas.mpl_connect('key_press_event', key_pressed)

plt.show()
