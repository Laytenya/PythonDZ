import time

def prod_matrix(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        l = []
        result = []
        for k in range(len(matrix1)):
            for i in range(len(matrix2[0])):
                sum = 0
                for j in range(len(matrix2)):
                    sum += matrix1[k][j] * matrix2[j][i]
                l.append(sum)
            result.append(l)
            l = []
        return result


def prod_mat_vec(matrix, vector):
    if len(matrix[0]) == len(vector):
        nested_list = []
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[i])):
                sum += (matrix[i][j] * vector[j])
            nested_list.append(round(sum, 3))
        return nested_list
    else:
        return ('Умножение невозможно!')



def sled(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum += matrix[i][j]
    return sum


def scalar_prod(vec1, vec2):
    prod  = 0
    for i in range(len(vec1)):
        prod += vec1[i] * vec2[i]
    return prod

def vector_gictagramm(vec, count):
    delta = (max(vec) - min(vec)) / count
    sorted(vec)
    for i in range(count):
        c = 1
        for j in vec:
            if min(vec) + delta * i <= j <= min(vec) + delta * (i + 1):
                c += 1
        print(f'{(min(vec) + delta * i):.1f} -- {(min(vec) + delta * (i + 1)):.1f} -- {c}')

def vector_filtration(vec, kernel):
    result = []
    for i in range(0, len(vec)-len(kernel) + 1):
        sum = 0
        for j in range(len(kernel)):
            sum += vec[i + j] * kernel[j]
        result.append(sum)
    return result

def read_file(link = 'D:\Python project\pythonProject1\example.txt'):
    with open(link, 'r') as file:
        print(file.read())


def write_file(link = 'D:\Python project\pythonProject1\example111.txt'):
    with open(link, 'a') as file:
        file.write('New words\n')
        new = input('Напишите что-нибудь!!!')
        file.write(new)
        print(new)

def timer(func):
    def wrapper(*arg):
        start = time.time()
        result = func(*arg)
        end = time.time()
        return (f' Результат функции - {result}, время расчета {(end - start):20f} ')
    return wrapper

if __name__ == '__main__':
    pass
