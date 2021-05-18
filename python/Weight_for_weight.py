def order_weight(string):
    bar = sorted(string.split(' '))
    baz = sorted(bar,key=foo)
    return " ".join(baz)


def foo(n):
    return sum(int(item) for item in n)