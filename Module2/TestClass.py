from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
import sys
import random
import math
import numpy as np
from numpy import array
import scipy.spatial.distance as ssd


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


"""

test_matrix = [[0, 12.3214, 64.2314],
               [12.3214, 0, 11.21],
               [64.2314, 11.21, 0]]
test_matrix_a = array(test_matrix)
dist_matrix = ssd.squareform(test_matrix_a)
print(dist_matrix)
"""

to_vector = [[3], [97, 96], [96, 98, 97], [96, 98, 97, 95], [98, 98, 97, 95, 98]]
one_list = []
for i in range(0, len(to_vector)):
    for j in range(0, len(to_vector[i])):
        one_list.append(to_vector[i][j])
a = np.array(one_list)
print(a)

Z = linkage(a, 'single')
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
#print(Z)

#build_matrix(points_array, matrix)
