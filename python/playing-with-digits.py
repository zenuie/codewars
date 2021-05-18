def dig_pow(n, p):
    k = p
    num = 0
    n = str(n)
    for i in n:
        i = int(i)
        num += i ** k
        k += 1
    if num % int(n) == 0:
        return num / int(n)
    else:
        return -1
