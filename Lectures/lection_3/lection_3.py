#ФУНКЦИИ
# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
    

# a = sum_numbers(5, 'qwerty')
# print(a)


##############
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'a', 'w'))



###############
# РЕКУРСИЯ на примере Фибоначи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)


###################
#ВИДЫ СОРТИРОВКИ

# Быстрая сортировка
# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой должен отгадать. Согласитесь, что мы можем перебирать эти значения в случайном порядке, например: 32, 27, 60, 73… Да, мы можем угадать в какой-то момент, но что если мы обратиться к стратегии “разделяй и властвуй” Обозначим друзей, друг_1 это Иван, который загадал число, друг_2 это Петр, который отгадывает. 

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]#проходим по всем элементам и брать только те, которые меньше или равны pivot 
#     greater = [i for i in array[1:] if i > pivot]#больше...
#     return quick_sort(less) + [pivot] + quick_sort(greater)
    
# print(quick_sort([1,2,3,45,6,23,78,91]))
# print(quick_sort([10,5,2]))


######### Сортировка слияния

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]#от начала
        right = nums[mid:]#от конца
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1    

list1 = [1,2,4,6,8,9,0,5,43,32]
merge_sort(list1)
print(list1)
