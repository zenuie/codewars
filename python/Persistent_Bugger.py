def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        total = 1
        n = list(map(int, str(n)))
        for i in n:
            total *= int(i)
        n = str(total)
        count += 1
    return count
