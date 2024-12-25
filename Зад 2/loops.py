'''

#1-1
while True:
    a, b = int(input()), int(input())
    print(a+b)


#1-2
count = 0
a = 1
for i in range(5):
    for j in range(5):
        if count % 2 == 0:
            print('*', end=' ')

        else:
            print(a, end=' ')
            a += 1
        count += 1
    print()
'''
'''
#1-3
min = int(input(('Нижняя граница :')))
max = int(input(('Верхняя граница :')))
print('интервал {} < x < {}'. format(min, max))

d = (min + max) // 2

while True:

    print('Число равно {}'.format(d))
    j = input('no/yes')

    if j == 'yes':
        print('Число равно  {}'.format(d))
        break

    else:
        print('Число больше {}'.format(d))
        i = input('no/yes')

        if i == 'yes':
            min = d
            d = (min+max)//2
            continue

        elif i == 'no':
            max = d
            d = (max+min)//2
            continue


'''
'''
#1-4
count = int(input())
a = 0
while count != 0:
    if a < count:
        a = count

    count = int(input())

print(a)
'''
'''
#1-5
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end = ' ')
    print()
'''

'''
#2-1
import random
rand_list = []
n = 10

for i in range(n):
    rand_list.append(random.randint(-1000, 1000))
print(rand_list)

rand_list.sort()

print('min',min(rand_list))
print('max',max(rand_list))

print('median', rand_list[(n-1)//2])

print(rand_list)
'''
'''
#2-2
import random
rand_list = []
n = 20

for i in range(n):
    rand_list.append(random.randint(0, 100))
print(rand_list)
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []
a10 = []
for i in rand_list:
    if 0 <= i <= 9:
        a1.append((i))
    elif  10 <= i <= 19:
        a2.append((i))
    elif 20 <= i <= 29:
        a3.append((i))
    elif 30 <= i <= 39:
        a4.append((i))
    elif 40 <= i <= 49:
        a5.append((i))
    elif 50 <= i <= 59:
        a6.append((i))
    elif 60 <= i <= 69:
        a7.append((i))
    elif 70 <= i <= 79:
        a8.append((i))
    elif 80 <= i <= 89:
        a9.append((i))
    elif 90 <= i <= 100:
        a10.append((i))

all_list = [a1, a2, a3, a4, a5, a6,a7, a8,a9, a10]
for j in range(len(all_list)):
    print(j, '-', len(all_list[j]))
'''
'''
#2-4
a = [[1,2,3], [4,5,6], [7,8,9]]
b = [[3,2,1], [6,5,4], [9,8,7]]
vector = [1, 2, 3]

c = []
sum = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        sum += a[i][j] * vector[j]
    c.append(sum)
    sum = 0
print(c)

#2-5
import random
rand_list = []
n = 10

for i in range(n):
    rand_list.append(random.randint(-10, 10))
print(rand_list)

a = []
for i in range(len(rand_list)):
    if rand_list[i] < 0:

    else:
        a.append(rand_list(i))

print(a)
'''


