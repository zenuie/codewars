import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if (math.sqrt(sq)) % 1 == 0:  # 用取1的餘數判別開根號是否為整數
        return (math.sqrt(sq) + 1) ** 2
    else:
        return -1
