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

# import time
#
# list = []
# n = int(input("Enter the number of elements in the array N:  "))
# for i in range(n):
#     list.append(int(input(f"Enter {i + 1} number: ")))
# x = int(input("Enter number Х: "))
# count = 0
# print(n)
# print(list)
# print(x)
# start = time.perf_counter()
# for i in range(n):
#     if list[i] == x:
#         count += 1
# print(f"-> {count}")
# end = time.perf_counter()
# time = end - start
# print(f"Script execution time: {time}")

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


# Задача 18: Требуется найти в массиве A[1 N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5


# import time
# num = int(input('Кол. чисел:'))
# a = []
# for i in range(num):
#     a.append(int(input(f"Enter {i + 1} number: ")))
# x = int(input('Заданное число:'))
# start = time.perf_counter()
# b = [abs(a[i]-x) for i in range(len(a))]
# print(num)
# print(a)
# print(x)
# print(f"-> {a[b.index(min(b))]}")
# end = time.perf_counter()
# time = end - start
# print(f"Script execution time: {time}")


# Задача 20: В настольной игре Scrabble каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12


# import time
#
# word = input(f"Enter a word: ")
# n = None
#
# start = time.perf_counter()
#
#
# def letter_cost(ch):
#     global n
#     ch = ch.upper()
#     if ch in " ":
#         n = 0
#     elif ch in "A E I O U L N S T R А В Е И Н О Р С Т":
#         n = 1
#     elif ch in "D G Д К Л М П У":
#         n = 2
#     elif ch in "B C M P Б Г Ё Ь Я":
#         n = 3
#     elif ch in "F H V W Y Й Ы":
#         n = 4
#     elif ch in "K Ж З Х Ц Ч":
#         n = 5
#     elif ch in "J X Ш Э Ю":
#         n = 8
#     elif ch in "Q Z Ф Щ Ъ":
#         n = 10
#     return n
#
#
# def word_counter():
#     word_count = 0
#     w_c = word.upper()
#     for i in w_c:
#         l_c = letter_cost(i)
#         word_count += l_c
#         print(f"{i} = {l_c}")
#     return word_count
#
#
# print(f"Output: {word_counter()}")
# print()
# end = time.perf_counter()
# time = end - start
# print(f"Script execution time: {time}")
