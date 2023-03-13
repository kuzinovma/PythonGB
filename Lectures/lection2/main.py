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
# Первый вариант
# a = (3, 4)
# print(a)
# print(a[0]) 
# обращаемя к конкретному числу по порядковому номеру

# Второй вариант
# a = (3, 4, 5)
# for item in a:
#     print(item)



# ###############
# Словари

# dictionary = {}
# dictionary = {
#     'up': '↑',
#     'left': '←',
#     'down': '↓',
#     'right': '→'
# }

# for k in dictionary.keys(): #если dictionary.values то выведет стрелки
#     print(k)

# можно вывести и символ и текст
# print(dictionary['up'])
# dictionary['up'] = 'up'
# print(dictionary['up'])


#####################

# Множества
# colors = {'red', 'green', 'blue'}
# print(colors) #r g b
# colors.add('red')
# print(colors) # r g b 
# colors.add('gray')
# print(colors) # r g b gray
# colors.remove('red')
# print(colors) # g b gray
# colors.discard('red') #ok
# print(colors) # g b gray
# colors.clear()
# print(colors) #set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() #1 2 3 5 8
# u = a.union(b) # 1 2 3 5 8 13 21
# i = a.intersection(b) # 8 2 5
# dl = a.difference(b) # 1 3
# dr = b.difference(a) # 13 21

# q = a \
#     .union(b) \
#         .difference(a.intersection(b))


#########
# Списки

# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

#Удаление последнего элемента

# list1  = [1,2,3,4,5]
# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# Вставляем элемент в между других элементов

list1 = [1,2,3,4,5]

print(list1.insert(2, 11))
print(list1)