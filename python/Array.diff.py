def array_diff(a, b):
    for i in b:
        for j in a:
            if i == j:
                while a.count(i):
                    a.remove(i)
    return a
