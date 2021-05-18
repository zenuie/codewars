def is_triangle(a, b, c):
    if a + b > c > abs(a - b):
        return True
    else:
        return False
