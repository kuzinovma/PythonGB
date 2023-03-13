# Ввод данных в файл
# Первый способ
# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('\nLine 2\n')
# data.write('Line 3\n')
# data.close

# Второй способ
# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
#     # с w не нужно принудительно закрывать (data.close)

# Вывод данных из файла
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()


#################
# Функции

# import helloPy

# print(helloPy.f(1))

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) #asdw
# print(concatenatio('a', '1'))  #a1
# # print(concatenatio(1, 2, 3, 4)) выдаст ошибку

##########
# Картежи
a = (3, 4)
print(a)
print(a[0]) #обращаемя к конкретному числу по порядковому номеру
