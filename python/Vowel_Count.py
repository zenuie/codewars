"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(sentence):
    a_conut = sentence.count('a')
    e_count = sentence.count('e')
    i_count = sentence.count('i')
    o_count = sentence.count('o')
    u_count = sentence.count('u')
    return a_conut + e_count + i_count + o_count + u_count
