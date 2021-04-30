def create_phone_number(n):
    n.insert(0, "(")
    n.insert(4, ") ")
    n.insert(8, "-")
    n = map(str, n)
    n = "".join(n)
    return n
