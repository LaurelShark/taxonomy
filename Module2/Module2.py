import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()
ax.plot(100, 1, 100)

matrix = [[0]]
tmp = [[], []]
print(matrix[0][0])


def compute_distances(arr):
    distance = math.sqrt((arr[0][0] - arr[0][1]) ** 2 + (arr[1][0] - arr[1][1]) ** 2)
    return distance


def append_matrix(arr, mtx):
    if len(mtx) < len(arr[0]):
        mtx.append([])
        print(mtx)
    for item in range(0, len(mtx) - 1):
        for i in range(0, len(arr[0]) - 1):
            for j in range(1, len(arr[1])):
                mtx[item][i] = math.sqrt((arr[i][i] - arr[i][j]) ** 2 + (arr[j][i] - arr[j][j]) ** 2)
                print(mtx[item][i])
    return mtx


def pick_up_point(event):
    if len(tmp) == 0:
        for i in range(0, 2):
            tmp.append([])
    x_point = event.xdata
    y_point = event.ydata
    print('picked: x = ' + str(x_point) + ', y = ' + str(y_point))
    tmp[0].append(x_point)
    tmp[1].append(y_point)
    if len(tmp[0]) >= 2:
        #dist = compute_distances(tmp)
        #print('distance is: ' + str(dist))
        new_matrix = append_matrix(tmp, matrix)
        print(new_matrix)


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))


mset = int(input('Enter the number of elements: '))

# cid = fig.canvas.mpl_connect('button_press_event', onclick)
cid = fig.canvas.mpl_connect('button_press_event', pick_up_point)
plt.show()
