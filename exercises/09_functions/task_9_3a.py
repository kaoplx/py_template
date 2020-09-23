# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename , 'r') as f:
        for line in f:
            if 'FastEthernet' in line:
                key = line.rstrip().strip('\n').split()[-1:]
            elif 'switchport access vlan ' in line:
                val = line.rstrip().strip('\n[]').split()[-1:]
                access_dict[str(key).strip("[]'")] = int(str(val).strip("\n[]'"))
            elif 'switchport mode access'in line:
                val = 1
                access_dict[str(key).strip("[]'")] = val
        f.seek(0)
        for line in f:
            value = []
            if 'FastEthernet' in line:
                key = line.rstrip().strip('\n').split()[-1:]
            elif 'trunk allowed vlan' in line:
                val = line.strip("\n").split(" ")[-1].split(',')
                for item in val:
                    value.append(int(item))
                trunk_dict[str(key).strip('[]"\'')] = value
    return (access_dict , trunk_dict)

file_name=r'C:\Users\ale-k\OneDrive\Desktop\gittest\py_template-1\exercises\09_functions\config_sw2.txt'

print(get_int_vlan_map(file_name))