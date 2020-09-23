# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
ip_addr = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]

def ping_ip_addresses(ip_addresses):
    av = []
    not_av = []
    for ip in ip_addresses:
        ping = subprocess.run(['ping' , ip , '-n' , '1'], stdout = subprocess.PIPE, stderr=subprocess.PIPE, encoding=('cp866'))
        if ping.returncode == 0:
            av.append(ip)
        else:
            not_av.append(ip)
    tuple_ip_av = tuple(av)
    tuple_ip_not_av = tuple(not_av)
    return (tuple_ip_av, tuple_ip_not_av)
if __name__ == "__main__":
    print(ping_ip_addresses(ip_addr))