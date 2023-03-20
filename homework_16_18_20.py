# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1 N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1


# 1st way with count

import time

list = []
n = int(input("Enter the number of elements in the array N:  "))
for i in range(n):
    list.append(int(input(f"Enter {i + 1} number: ")))
x = int(input("Enter number Х: "))
count = 0
print(n)
print(list)
print(x)
start = time.perf_counter()
for i in range(n):
    if list[i] == x:
        count += 1
print(f"-> {count}")
end = time.perf_counter()
time = end - start
print(f"Script execution time: {time}")

# 2nd way without count

# import random
# import time
#
# len_list = int(input("Enter the number of elements in the array N: "))
# x_num = int(input("Enter number X: "))
#
# start = time.perf_counter()
# num_list = [random.randint(1, 10) for _ in range(len_list)]
# print(len_list)
# print(num_list)
# print(x_num)
# print(f'-> {num_list.count(x_num)}')
# end = time.perf_counter()
# time = end - start
# print(f"Script execution time: {time}")
