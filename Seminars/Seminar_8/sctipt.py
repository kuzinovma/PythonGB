from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Такого варианта нет!')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('\nВывожу данные для Вас из 1-ого файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_v2 = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_v2.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_v2
        print(''.join(data_first))
        # print(*data_first, sep='')

    print('\nВывожу данные для Вас из 2-ого файла: \n')
    with open('data_second_variant.csv', 'r+', encoding='utf-8') as file:
        data_second = file.readlines()
        data_second_version_second = []
        j = 0
        for i in range(len(data_second)):
            if data_second[i] == '\n' or i == len(data_second)-1:
                data_second = data_second_version_second.append(''.join(data_second[j:i+1]))
                j = i
        data_second = data_second_version_second
        print(''.join(data_second))
    return data_first, data_second

def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        # ТУТ НАПИСАТЬ КОД
        print('Меняем: ', data_first[number_journal-1])
        with open('data_first_variant.csv', 'r', encoding='UTF-8') as file:
            data_first = file.readlines()

        if number_journal !=1:
            start = (number_journal - 1)*5
        else:
            start = number_journal - 1
        print('Что нужно поменять?\n\n'
              '1. Имя\n '
              '2. Фамилия\n '
              '3. Номер\n '
              '4. Адрекс\n ')
        command = int(input('Введит номер из списка: '))
        while command < 1 or command > 4:
            print('Такого варианта в списке нет!')
            command = int(input('Введит номер из списка: '))

        if command == 1:
            data_first[start] = name_data() + '\n'
        elif command == 2:
            data_first[start + 1] = surname_data() + '\n'
        elif command == 3:
            data_first[start + 2] = phone_data() + '\n'
        else:
            data_first[start +3] = address_data() + '\n'

        with open('data_first_variant.csv', 'w', encoding='UTF-8') as file:
            file.write(''.join(data_first))

    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        # ТУТ НАПИСАТЬ КОД
        print('Меняем: ', data_second[number_journal - 1])
        contact = data_second[number_journal - 1].split(','
        )
        print('Что нужно поменять?\n\n'
              '1. Имя\n '
              '2. Фамилия\n '
              '3. Номер\n '
              '4. Адрекс\n ')
        command = int(input('Введит номер из списка: '))

        while command < 1 or command > 4:
            print('Такого варианта в списке нет!')
            command = int(input('Введит номер из списка: '))

        if command == 1:
            contact[0] = '\n' + name_data()
        elif command == 2:
            contact[1] = surname_data()
        elif command == 3:
            contact[2] = phone_data()
        else:
            contact[3] = address_data() + '\n'

        data_second[number_journal - 1] = ','. join(contact)

        with open('data_second_variant.csv', 'w', encoding='UTF-8') as file:
            file.write(''.join(data_second))


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Такого варианта в списке нет!')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД
        delete_element = data_first.pop(number_journal -1)
        print('Удаляем: ', delete_element)

        data_first_v2 = []
        for item in data_first:
            if item.startswith('\n'):
                data_first_v2.append(item[1:])
            else:
                data_first_v2.append(item)
        data_first = data_first_v2        

        with open('data_first_variant.csv', 'w', encoding='UTF-8') as file:
            file.write(''.join(data_first))
    
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД
        delete_element = data_second.pop(number_journal - 1)
        print('Удаляем', delete_element)

        data_second_v2 = []
        for item in data_second:
            if item.startswith('\n'):
                data_second_v2.append(item[1:])
            else:
                data_second_v2.append(item)
        data_second = data_second_v2

        with open('data_second_variant,csv', 'w', encoding='UTF-8') as file:
            file.write(''.join(data_second))