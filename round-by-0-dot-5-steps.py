import math


def solution(n):
    integer = math.floor(n)
    # your code here
    if n % 1 < 0.25:
        return math.floor(n)
    elif n % 1 < 0.75:
        integer += 0.5
        return integer
    else:
        return math.ceil(n)
