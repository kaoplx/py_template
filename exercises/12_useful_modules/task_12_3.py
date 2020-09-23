# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

Для этого задания нет тестов
"""

ip_reachble = ['10.1.1.1' , '192.168.5.5']
ip_unreachble = ['134.134.143.1', '99.99.8.8']

from tabulate import tabulate
def print_ip_table(ip_r , ip_unr):
    table = [ip_r , ip_unr]
    header = ['reachable', 'unreacheble']
    return tabulate(table , header, stralign='center' , tablefmt='pipe')

if __name__ == "__main__":
    print(print_ip_table(ip_reachble, ip_unreachble))