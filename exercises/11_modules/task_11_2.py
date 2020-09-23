# -*- coding: utf-8 -*-
from draw_network_graph import *
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology. Если функция parse_cdp_neighbors не может обработать вывод
одного из файлов с выводом команды, надо исправить код функции в задании 11.1.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

# эти заготовки написаны чтобы показать в какой момент должна
# рисоваться топология (после вызова функции)

def create_network_map(filenames):
    d = {}
    for filename in filenames:
        with open(r"C:\Users\ale-k\OneDrive\Desktop\gittest\py_template-1\exercises\11_modules\\" + filename , 'r') as f:
            '''получаем имя своего устройства'''
            string = f.read()
            f.close()
            device_name = string.strip().split('\n')[0]
            device_name = device_name.split(">")[0]
            '''формируем словарь'''
            parse_str = string.strip().split('Port ID')[1].strip().split('\n')
            
            for item in parse_str:
                l_item = item.split()
                key = (device_name , l_item[1] + l_item[2])
                d[key] = (l_item[0] , l_item[-2] + l_item[-1])
    list_item=[]
    for item in d.keys():
        list_item.append(item)
    for item in list_item:
        if item in d.values():
            del d[item]
    return  d

    


if __name__ == "__main__":
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]

    topology = create_network_map(infiles)
    # рисуем топологию:
    draw_topology(topology)
