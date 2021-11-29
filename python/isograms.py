"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter casing)
"""


def is_isogram(string):
    string = string.lower()
    lst = []
    for i in string:
        lst.append(i)
    return len(set(lst)) == len(string)


