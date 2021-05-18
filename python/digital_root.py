def digital_root(n):
    result = 10
    while len(str(result)) > 1:
        result = 0
        for i in str(n):
            result += int(i)
        n = result
    return result
