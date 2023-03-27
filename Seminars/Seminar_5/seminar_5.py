#Задача 35
# Даны два цеых числа А и В
# Выведите все числа А и В включительно, в порядке возрастания, если А <В или в порядке убывания, если А < В
# def print_number(a, b):
#     if a == b:
#         return f"{a}"
#     if a > b:
#         return f"{a}, {print_number(a - 1, b)}"
#     if a < b:
#         return f"{a}, {print_number(a + 1, b)}"


# print(print_number(1, 5))
# print(print_number(10, 20))

############
# """Последовательностью Фибоначчи называется последовательность  чисел a0, a1, ..., an, ..., где  a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи"""
# 1 Вариант
# def fib_rec(n):
#     if n <= 1:
#         return n
#     else:
#         return fib_rec(n - 1) + fib_rec(n - 2)

# print(fib_rec(10))

# 2 Вариант
# cahce = {}
# # My - Memo
# def fib_rec_cache(n):
#     if n not in cahce:
#         cahce[n] = n if n <= 1 else fib_rec_cache(n - 1) + fib_rec_cache(n - 2)
#     return cahce[n]

# Задача 33. 
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.  Напишите программу, которая заменяет оценки Василия, но наоборот:  все максимальные – на минимальные.

# Вариант 1 - max and min
list_1 = [2, 2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]
max_number = max(list_1)
min_number = min(list_1)

for i in range(len(list_1)):
    if list_1[i] == max_number:
        list_1[i] = min_number
        
print(list_1)


# Вариант 2 - Свой max, min
# list_1 = [2, 2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]
# min_number, max_number = float('inf'), float('-inf')

# for num in list_1:
#     if num > max_number:
#         max_number = num
#     elif num < min_number:
#         min_number = num
        
# print(f'Т - {min_number}, И - {max_number}')

# for i in range(len(list_1)):
#     if list_1[i] == max_number:
#         list_1[i] = min_number
# print(list_1)