def area_tri(a,b):
    from math import sqrt,pi
    c = sqrt(a**2+b**2)
    r = (a + b - c) / 2
    print(abs((pi*r**2)-((a*b)/2)))
    return abs((pi*r**2)-((a*b)/2))