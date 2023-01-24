import os


def menu(menuitems):
    for i in menuitems:
        print(f'{i[0]} - {i[1]}')    
    text = input("Введите номер меню:> ")
    return text


def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result 

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')

def clear_screen():
    os.system('cls')


def print_bus():
    clear_screen()
    print ('| Автобус|   Госномер |')
    print('='*23)
    for element1, element2 in read_data_from_file('bus.txt'):
        print ('|{:>7} |{:>12}|'.format(element1, element2))
        print('-'*23)

    addit = input("Что хотите сделать дальше?\n m - выход в основное меню\n q - выход из программы\n >: ")
    if addit == 'm':
        clear_screen()
    elif addit == 'q':
        exit()


def add_bus():
    clear_screen()
    save_data_to_file('bus.txt', input("Введите параметры автобуса: "))
    while True:
        clear_screen()

        print ('| Автобус|   Госномер |')
        print('='*23)
        for element1, element2 in read_data_from_file('bus.txt'):
            print ('|{:>7} |{:>12}|'.format(element1, element2))
            print('-'*23)
        
        question = input("\nХотите добавить еще?\ny - да\nn - выход в главное меню\n :> ")
        if question == 'y':
            clear_screen()
            add_bus()
        elif question == 'n':
            clear_screen()
            return


def print_drivers():
    clear_screen()
    print ('| ID водителя|   Фамилия |')
    print('='*26)
    for element1, element2 in read_data_from_file('drivers.txt'):
        print ('|{:>11} |{:>11}|'.format(element1, element2))
        print('-'*26)

    addit = input("Что хотите сделать дальше?\nm - выход в основное меню\nq - выход из программы\n >: ")
    if addit == 'm':
        clear_screen()
    elif addit == 'q':
        exit()


def add_driver():
    clear_screen()
    save_data_to_file('drivers.txt', input("Введите параметры водителя: "))
    while True:
        print ('| ID водителя|   Фамилия |')
        print('='*26)
        for element1, element2 in read_data_from_file('drivers.txt'):
            print ('|{:>11} |{:>11}|'.format(element1, element2))
            print('-'*26)

        question = input("Хотите добавить еще?\ny - да\nn - выход в главное меню\n :> ")
        if question == 'y':
            add_driver()
            print(read_data_from_file('drivers.txt'))
        elif question == 'n':
            clear_screen()
            return

def print_route():
    clear_screen()

    print ('| Маршрут|   № |    Госномер | Водитель |')
    print('='*42)
    for element1, element2, element3, element4 in read_data_from_file('route.txt'):
        print ('|{:>7} |{:>4} |{:>12} |{:>9} |'.format(element1, element2, element3, element4))
        print('-'*42)

    question = input("Вывести детали маршрута подробнее?\ny - да\nn - возврат в главное меню\n >: ")
    if question == 'y':
        clear_screen()

        i = 0
        j = 0
        k = 0
        route = read_data_from_file('route.txt')
        bus = read_data_from_file('bus.txt')
        drivers = read_data_from_file('drivers.txt')

        while i < len(route):
            while j < len(bus):
                if route[i][2] == bus[j][0]:
                    route[i][2] = bus[j][1]
                else:
                    j += 1
            j = 0
            i += 1

        i = 0
        while i < len(route):
            while k < len(drivers):
                if route[i][3] == drivers[k][0]:
                    route[i][3] = drivers[k][1]
                else:
                    k += 1
            k = 0
            i += 1

        print ('| Маршрут|   № |    Госномер | Водитель |')
        print('='*42)
        for element1, element2, element3, element4 in route:

            print ('|{:>7} |{:>4} |{:>12} |{:>9} |'.format(element1, element2, element3, element4))
            print('-'*42)

        with open('detailed_road.txt', 'w', encoding='utf8') as filehandle:  
            for listitem in route:
                filehandle.write('%s\n' % listitem)

        addit = input("Что хотите сделать дальше?\n m - выход в основное меню\n q - выход из программы\n >: ")
        if addit == 'm':
            clear_screen()
        elif addit == 'q':
            print("Всего хорошего!")
            exit()

    elif question == 'n':
        clear_screen()



def add_route():
    save_data_to_file('route.txt', input("Введите параметры маршрута: "))
    while True:
        print ('| Маршрут|   № |    Госномер | Водитель |')
        print('='*42)
        for element1, element2, element3, element4 in read_data_from_file('route.txt'):

            print ('|{:>7} |{:>4} |{:>12} |{:>9} |'.format(element1, element2, element3, element4))
            print('-'*42)

        question = input("Хотите добавить еще?\ny - да\nn - выход в главное меню\n :> ")
        if question == 'y':
            clear_screen()
            add_route()
            print(read_data_from_file('route.txt'))
        elif question == 'n':
            clear_screen()
            return