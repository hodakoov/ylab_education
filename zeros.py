'''
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:
Будьте осторожны 1000! имеет 2568 цифр.
Доп. инфо: http://mathworld.wolfram.com/Factorial.html
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
'''


def zeros(n: int):
    summa, count, i = 0, None, 1

    while count != 0:
        count = n // 5 ** i
        summa += count
        i += 1
    return summa


"""
Для проверки:

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

"""
