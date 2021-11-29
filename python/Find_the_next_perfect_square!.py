'''
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
'''

import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if (math.sqrt(sq)) % 1 == 0:  # 用取1的餘數判別開根號是否為整數
        return (math.sqrt(sq) + 1) ** 2
    else:
        return -1
