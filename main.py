import os
import function as fn

fn.clear_screen()

menuitems = [
        ("1", "Вывод автобусов"),
        ("2", "Добавление автобуса"),
        ("3", "Вывод водителей"),
        ("4", "Добавление водителей"),
        ("5", "Вывод маршрута"),
        ("6", "Добавление маршрута"),
        ("7", "Выход")]

while True:
    text = fn.menu(menuitems)

    if text == '1':
        fn.print_bus()


    elif text == '2':
        fn.add_bus()


    if text == '3':
        fn.print_drivers()


    if text == '4':
        fn.add_driver()


    if text == '5':
        fn.print_route()


    if text == '6':
        fn.clear_screen()
        fn.add_route()


    if text == '7':
        print("Всего хорошего!")
        quit()