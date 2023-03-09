# n = 5
# print(type(n))

# n = 'fd"123"fd'
# print(n)

# print(5)
# print(5)
# print(5)
# print(c)аша
# a = 5
# b = 5.89
# c = "hello"

# # print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))


# print('Введите первое число')
# a = int(input())
# b = int(input('Введите второе число: '))

# print(a, '+', b, '=', a+b)

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))



# a = 5.89956
# b = 6.556554
# print(round(a*b, 3))



# a=1>4
# print(a)

# a=1<4 and 5>2
# print(a)

# a=1==2
# print(a)

# a=1 !=2
# print(a)

# a='qwe'
# b='qwe'
# print(a==b)

# a=1<3<5<10
# print(a)



# username = input('Введите ваше имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')    
# else:
#     print('Привет, ', username)    



# i = 0
# while i < 5:
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит')
# print(i)



# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: #если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: #делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1



# r = range(100, 0, -20)
# for i in r:
#     print(i)



# line - ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)



# text = 'СъеШь ещЕ эТИх булОК'
# print(len(text))
# print('еще' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('еще', 'ЕЩЕ'))



text = 'съешь ещё этих мягких французских булок'
print(text[0])                            #с
print(text[1])                            #ъ
print(text[len(text)-1])                  #к
print(text[-1])
print(text[-5])                           #б
print(text[:])                            #съешь ещё этих мягких французских булок
print(text[:2])                           #съ
print(text[len(text)-2:])                 #ок
print(text[2:9])                          #ешь ещё
print(text[6:-18])                        #ещё этих мягких
print(text[0:len(text):6])                #сеикакл
print(text[::6])                          #сеикакл
text = text[2:9] + text[-5] + text [:2]   #...
print(text)