"""
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:
2149583361 -> "128.32.10.1"
32         -> "0.0.0.32"
0          -> "0.0.0.0"
"""


def int32_to_ip(int32: int):
    ip = []
    for i in range(1, 5):
        ip.insert(0, str(int32 % 256))
        int32 //= 256
    result = '.'.join(ip)
    return result


"""
Для проверки:

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
"""
