"""     Задача 16: Требуется вычислить, сколько раз встречается 
некоторое число X в массиве A[0..N-1]. Пользователь в первой 
строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел A[i]. Последняя строка 
содержит число X
Пример:
N = 5
1 2 3 4 5
X = 3
-> 1                                                            """

import random

N = int(input('Введите N (размер массива): '))

A = [0] * N

for i in range(len(A)):
    A[i] = random.randint(0, 9)
print(A)

X = int(input('Введите X (число в массиве): '))

count = 0
for i in range(0, len(A)):
    if X == A[i]:
        count += 1
print(count)
