from math import sqrt, ceil
from functools import reduce


def list_squared(m, n):
    result = []
    for number in range(m, n + 1):  # 求因數目標
        if sqrt(factors(number)) == ceil(sqrt(factors(number))):
            result.append([number, factors(number)])


def factors(n):
    square_number = 0
    for i in set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))):
        square_number += i ** 2
    return square_number


list_squared(1, 250)
