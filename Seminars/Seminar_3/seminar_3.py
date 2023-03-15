# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# import random
# numbers = [random.randint(0, 10) for _ in range(10)] #чтобы вывести рандомные значения

# Вариант 1
# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# result = []
# for num in numbers:
#     if num not in result:
#         result.append(num) # внутрь массива помещает то, что впишем в скобки вместо num
# print(len(result))

# Вариант 2
# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# result = []
# for num in numbers:
#     if result.count(1) == 0:
#         result.append(num) 
# print(len(result))

# Вариант 3
# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# numbers_copy = numbers.copy()
# for num in numbers.copy():
#     while numbers.count(num) != 1:
#         numbers.remove(num)
# print(len(numbers))

#Вариант 4
# print(len(set(numbers)))


##########################
# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# numbers = [1, 2, 3, 4, 5, 6]
# k = 3
# k = k % len(numbers)

#Вариант 1
# list_result = []
# len_list = len(numbers)
# for i in range(len_list - k, len_list):
#     list_result.append(numbers[i])
# for i in range(len_list - k):
#     list_result.append(numbers[i])
# print(list_result)

#Вариант 2
# list_result = []
# for i in range(len(numbers)):
#     list_result.append(numbers[-k + i])
# print(list_result)

#Вариант 3
# for _ in range(k):
#     numbers.insert(0, numbers.pop())#pop удаляет последний элемент
# print(numbers)

#Вариант 4
# print(numbers[-k:] + numbers[:-k])

###################
# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list_1 = [{"V": "S001", "V12": "S0012"}, {"V": "S002"}, {"VI": "S001"},
#           {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# # Вариант 1 - original
# unique_kyes = set()
# for value in list_1:
#     for key in value:
#         unique_kyes.add(value[key])
# print(unique_kyes)


# # Вариант 2
# unique_kyes = set()
# for value in list_1:
#     unique_kyes.update(value.values())
# print(unique_kyes)



# ПРИМЕР СЛОВАРЯ!!!!!!!!!
# d = {'Alex': 21, 'Dima': 25, 'Sveta': 27}
# list_dicts = [{'Alex': 21, 'Dima': 25, 'Sveta': 27}, {'Alex': 'Cv', 'Dima': 'NLP', 'Sveta': "ML"}]
# print(list_dicts[1]['Sveta'], list_dicts[0]['Sveta'])

##################
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)

# numbers = [0, 1, 5, 2, 3]

# #Вариант 1
# count = 0
# for i in range(0, len(numbers)):
#     if numbers[1] > numbers[i - 1]:
#         count += 1
# print(count)
