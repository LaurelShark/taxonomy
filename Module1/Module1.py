import sys
import random


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


print("Welcome to matrix program!")
mset = int(input("Enter the number of elements for clusterization: "))
num1 = int(input("Please, enter first value: "))
print("Good.")
num2 = int(input("Enter second value: "))
auto = input("Enable auto-filling? (y/n)")

matrix = [[],
          []]
matrix[0].append(num1)
matrix[1].append(num2)

if auto == "y":
    auto_fill()
else:
    manual()
