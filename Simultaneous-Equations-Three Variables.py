
def solve_eq(eq):
    count = 0
    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    z1 = 0
    z2 = 0
    z3 = 0
    equlX = 0
    equlY = 0
    equlZ = 0

    for i in eq:
        for j in i:
            count += 1
            if count == 1:
                x1 += j
            elif count == 2:
                x2 += j
            elif count == 3:
                x3 += j
            elif count == 5:
                y1 += j
            elif count == 6:
                y2 += j
            elif count == 7:
                y3 += j
            elif count == 9:
                z1 += j
            elif count == 10:
                z2 += j
            elif count == 11:
                z3 += j
            elif count == 4:
                equlX += j
            elif count == 8:
                equlY += j
            elif count == 12:
                equlZ += j
    cramer = (x1 * y2 * z3 + y1 * z2 * x3 + z1 * x2 * y3) - x3 * y2 * z1 - y3 * z2 * x1 - z3 * x2 * y1
    deltaX = (equlX * y2 * z3 + equlY * z2 * x3 + equlZ * x2 * y3) - x3 * y2 * equlZ - y3 * z2 * equlX - z3 * x2 * equlY
    deltaY = (x1 * equlY * z3 + y1 * equlZ * x3 + z1 * equlX * y3) - x3 * equlY * z1 - y3 * equlZ * x1 - z3 * equlX * y1
    deltaZ = (x1 * y2 * equlZ + y1 * z2 * equlX + z1 * x2 * equlY) - equlX * y2 * z1 - equlY * z2 * x1 - equlZ * x2 * y1
    ansX = deltaX // cramer
    ansY = deltaY // cramer
    ansZ = deltaZ // cramer
    return [ansX, ansY, ansZ]
