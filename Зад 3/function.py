#1
'''
print('Введите *, если необходима таблица умножения',
          'Введите /, если необходима таблица деления',
          'Введите +, если необходима таблица сложения',
          'Введите -, если необходима таблица вычитания', sep = '\n')
i = input()
'''
def func(s):
    if s == '*':
        print('Таблица умножения')
        for i in range(1, 10):
            for j in range(1, 10):
                print (f'{i} * {j} = {(i * j):<3}', end = ' ')
            print()

    if s == '/':
        print('Таблица деления')
        for i in range(1, 10):
            for j in range(1, 10):
                print(f'{i * j} / {j} = {i:<3}', end = '  ')
            print()

    if s == '+':
        print('Таблица сложения')
        for i in range(1, 10):
            for j in range(1, 10):
                print(f'{i} + {j} = {i+j:<3}', end = '  ')
            print()

    if s == '-':
        print('Таблица деления')
        for i in range(1, 10):
            for j in range(1, 10):
                if (i - j) <= 0:
                    print(f'{j} - {i} = {j - i:<3}', end = '  ')
                else:
                    print(f'{i} - {j} = {i - j:<3}', end='  ')
            print()
print('-----------------------------------------------Задание 1------------------------------------------------------')
func('*')
func('-')
func('+')
func('/')

#2-a
import random

def vector(n):
    a = list()
    for _ in range(n):
        a.append(round(random.uniform(0,1), 3))
    return a
print('-----------------------------------------------Задание 2A------------------------------------------------------')
print(vector(3))

#2-b
def matrix(m , n):
    nested_list = []
    for i in range(m):
        inner_list = []

        for j in range(n):
            inner_list.append(round(random.uniform(0, 1), 3))
        nested_list.append(inner_list)

    return nested_list

print('-----------------------------------------------Задание 2B------------------------------------------------------')
print(matrix(3,4))

#2-c

def prod(vector, matrix):
    if len(matrix[0]) == len(vector):
        nested_list = []
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[i])):
                sum += (matrix[i][j] * vector[j])
            nested_list.append(round(sum, 3))
        return nested_list
    else:
        print('Невыполнимая крманда')

print('-----------------------------------------------Задание 2C------------------------------------------------------')
print(prod(vector(3), matrix(3,3)))

#2-d
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = '  ')
        print()

def print_vector(vec):
    for i in range(len(vec)):
        print(vec[i])

def sum_diag(matrix):
    import numpy as np
    b = np.asarray(matrix)
    c = np.fliplr(b)
    print(f'Sum prime diagonal: {np.trace(b):.3} \nSum second diagonal: {np.trace(c):.3}')

print('-----------------------------------------------Задание 2D------------------------------------------------------')
print(print_matrix(matrix(3, 3)))
print(print(*vector(3)))
print(sum_diag(matrix(3,3)))



#2-g
def svertka(data, kernel):
    result = []
    conc = []
    for n in range(len(data) - len(kernel) + 1):
        for m in range(len(data[n]) + 1 - len(kernel[0])):
            sum = 0
            for i in range(len(kernel)):
                for j in range(len(kernel[i])):
                    sum += kernel[i][j] * data[i + n][j + m]
            result.append(sum)
        conc.append(result)
        result = []

    return conc
print('-----------------------------------------------Задание 2G------------------------------------------------------')
print(svertka(matrix(3, 4), matrix(2,2)))

#3
def decorator(func):
    def wrapper(kernel, *arg):
        result = []
        for i in range(len(arg)):
            result.append(func(arg[i], kernel))
        return result
    return wrapper


@decorator
def diff(data, kernel):
    return svertka(data, kernel)
    res = []
    for i in range(len(arg)):
        res.append(svertka(arg[i], kernel))
    print(res)

print('-----------------------------------------------Задание 3------------------------------------------------------')
print(diff(matrix(2,2), matrix(3,3), matrix(4,4)))

#4
# 0 - RGB, 1 - YIQ
color_vector = [0.5, 0.3, 0.4, 1]
def convert_color(color_vector):
    r, g, b, color_type = color_vector

    if color_type == 0:
        y = 0.299 * r + 0.587 * g + 0.114 * b
        i = 0.596 * r - 0.274 * g - 0.322 * b
        q = 0.211 * r - 0.522 * g + 0.311 * b

        return (f'Y = {y:.3},\nI = {i:.3},\nQ = {q:.3},\ntype = YIQ')
    elif color_type == 1:
        y, i, q = r, g, b
        r = y + 0.956 * i + 0.623 * q
        g = y - 0.272 * i - 0.648 * q
        b = y - 1.105 * i + 1.705 * q
        return (f'R = {r:.3},\nG = {g:.3},\nB = {b:.3}, \ntype = RGB')

print('-----------------------------------------------Задание 4------------------------------------------------------')
print(convert_color(color_vector))
