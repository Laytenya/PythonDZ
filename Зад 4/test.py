import time
import operation.first_modul as fp

start_time = time.time()
#1A
a = [[1,2,3], [4,5,6], [7,8,9]]
b = [[9,8,7], [6,5,4], [3,2,1]]
fp.prod_matrix(a, b)

# 1B
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vec = [1, 2, 3]
print(fp.prod_mat_vec(a, vec))

#1C
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(fp.sled(a))

#1D
vec1 = [1, 1, 1]
vec2 = [1, 1, 1]
print(fp.scalar_prod(vec1, vec2))

# 1E
vec = [1.1, 2.3, 3.5, 4.7, 5.9]
fp.vector_gictagramm(vec, 3)
# 1F
vec = [1,2,3,4,5]
kernel = [-1, 0, -1]
print(fp.vector_filtration(vec, kernel))

# 1G
fp.read_file('D:\Python project\pythonProject1\example.txt')
fp.write_file('D:\Python project\pythonProject1\example.txt')

# 2
print('------------------------test------------------------------')
# test 1A

a = [[1, 1, 0], [2, -1, 2]]
b = [[2, 1], [0, 3], [1, 2]]

c = [[1,2, 1],[1,2, 1]]
c1 = [[1,2],[1,2],[1,2]]

@fp.timer
def func(a,b):
    return fp.prod_matrix(a,b)
print(func(a,b),func(c,c1), sep='\n')

# test 1B
a1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vec1 = [1, 2, 3]
a2 = [[1, 2, 3], [4, 5, 6]]
vec2 = [1, 2]

@fp.timer
def func(a,b):
    return fp.prod_mat_vec(a,b)
print(func(a1,vec1),func(a2,vec2), sep='\n')

# test 1C
@fp.timer
def func(a):
    return fp.sled(a)
print(func(a1), sep='\n')

# test 1D
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

v1 = [1, 2]
v2 = [3, 4]
@fp.timer
def func(a, b):
    return fp.scalar_prod(a, b)
print(func(vec1, vec2), func(v1, v2), sep='\n')

# test 1E
@fp.timer
def func(a, b):
    return fp.vector_gictagramm(a, b)
vec = [1.1, 2.3, 3.5, 4.7, 5.9]
print(func(vec, 3))

# test 1F
vec = [1,2,3,4,5]
kernel = [-1, 0, -1]
@fp.timer
def func(a, b):
    return fp.vector_filtration(a, b)
print(func(vec, kernel))

# test 1G
@fp.timer
def func(link = ''):
    return fp.read_file(link), fp.write_file(link)
func('D:\Python project\pythonProject1\example.txt')


end_time = time.time()
elapse = end_time - start_time
print(f'Время выполнения всего основного блока кода: {elapse:.10f}')

# ускорение
from joblib import parallel_backend

def mt_example():
    import time
    start = time.time()
    with parallel_backend('threading', n_jobs=2):
        # 1A
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        print(fp.prod_matrix(a, b))
        # 1B
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        vec = [1, 2, 3]
        print(fp.prod_mat_vec(a, vec))
        # 1C
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(fp.sled(a))
        # 1D
        vec1 = [1, 1, 1]
        vec2 = [1, 1, 1]
        print(fp.scalar_prod(vec1, vec2))
    end = time.time()

    print(f'Time -- {(end - start):.10f}')
mt_example()


